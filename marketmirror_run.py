import os

import json

import requests

from datetime import datetime, timezone, timedelta



API_KEY = os.getenv("FINNHUB_API_KEY")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")



WATCHLIST = ["SPY", "QQQ", "NVDA", "GLD", "SLV", "USO", "XOM", "CVX", "BAC"]



os.makedirs("data", exist_ok=True)

os.makedirs("logs", exist_ok=True)

os.makedirs("state", exist_ok=True)





def send_telegram(message):

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:

        print("Telegram variables missing.")

        return False



    try:

        r = requests.post(

            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",

            data={

                "chat_id": TELEGRAM_CHAT_ID,

                "text": message,

            },

            timeout=15,

        )

        print("Telegram status:", r.status_code)

        return r.status_code == 200

    except Exception as e:

        print("Telegram error:", e)

        return False





def can_send_alert():

    state_file = "state/last_alert.json"



    if not os.path.exists(state_file):

        return True



    try:

        with open(state_file, "r") as f:

            state = json.load(f)



        last_time = datetime.fromisoformat(state["timestamp"])

        now = datetime.now(timezone.utc)



        return (now - last_time) >= timedelta(hours=1)



    except Exception:

        return True





def save_alert_timestamp():

    with open("state/last_alert.json", "w") as f:

        json.dump(

            {"timestamp": datetime.now(timezone.utc).isoformat()},

            f,

            indent=2,

        )





snapshot = {

    "timestamp_utc": datetime.now(timezone.utc).isoformat(),

    "source": "Finnhub",

    "watchlist": {},

}



for symbol in WATCHLIST:

    r = requests.get(

        "https://finnhub.io/api/v1/quote",

        params={"symbol": symbol, "token": API_KEY},

        timeout=15,

    )



    data = r.json()



    current = data.get("c")

    previous_close = data.get("pc")



    change = None

    change_pct = None



    if current and previous_close:

        change = round(current - previous_close, 4)

        change_pct = round(((current - previous_close) / previous_close) * 100, 4)



    snapshot["watchlist"][symbol] = {

        "current": current,

        "open": data.get("o"),

        "high": data.get("h"),

        "low": data.get("l"),

        "previous_close": previous_close,

        "change": change,

        "change_pct": change_pct,

        "raw": data,

    }





with open("data/market_snapshot.json", "w") as f:

    json.dump(snapshot, f, indent=2)





w = snapshot["watchlist"]

flags = []

level = "No alert"



spy = w["SPY"]["change_pct"]

qqq = w["QQQ"]["change_pct"]

nvda = w["NVDA"]["change_pct"]

gld = w["GLD"]["change_pct"]

slv = w["SLV"]["change_pct"]

uso = w["USO"]["change_pct"]

xom = w["XOM"]["change_pct"]

cvx = w["CVX"]["change_pct"]

bac = w["BAC"]["change_pct"]



if spy is not None and qqq is not None and nvda is not None:

    if spy > 0 and qqq > 0 and nvda < 0:

        flags.append("SPY and QQQ positive while NVDA is negative: possible AI leadership weakness.")



if gld is not None and gld > 1:

    flags.append("GLD above +1%: possible defensive/inflation/fear positioning.")



if uso is not None and uso < -1:

    flags.append("USO below -1%: energy complex under pressure.")



if xom is not None and xom < -1:

    flags.append("XOM below -1%: institutional energy weakness.")



if bac is not None and bac > 1:

    flags.append("BAC above +1%: financials supporting risk appetite.")



flag_count = len(flags)



if flag_count >= 6:

    level = "Level 4 — High Conviction"

elif flag_count >= 4:

    level = "Level 3 — Early Warning"

elif flag_count >= 2:

    level = "Level 2 — Increased Attention"

elif flag_count >= 1:

    level = "Level 1 — Observation"





report = []

report.append("MarketMirrorAI Automatic Review")

report.append(f"Timestamp UTC: {snapshot['timestamp_utc']}")

report.append("")

report.append("Watchlist:")



for symbol in WATCHLIST:

    report.append(

        f"- {symbol}: {w[symbol]['change_pct']}% | Current: {w[symbol]['current']}"

    )



report.append("")

report.append(f"Alert Status: {level}")

report.append(f"Flags detected: {flag_count}")



if flags:

    report.append("")

    report.append("Flags:")

    for item in flags:

        report.append(f"- {item}")



report_text = "\n".join(report)



with open("data/market_analysis.txt", "w") as f:

    f.write(report_text)



with open("logs/marketmirror.log", "a") as f:

    f.write("\n\n" + "=" * 60 + "\n")

    f.write(report_text)



print(report_text)



if level in ["Level 3 — Early Warning", "Level 4 — High Conviction"]:

    if can_send_alert():

        telegram_message = "ALERT: MarketMirrorAI Alert\n\n" + report_text

        sent = send_telegram(telegram_message)



        if sent:

            save_alert_timestamp()

            print("Telegram alert sent.")

        else:

            print("Telegram alert failed.")

    else:

        print("Telegram alert suppressed (anti-spam).")

else:

    print("No Telegram alert required.")

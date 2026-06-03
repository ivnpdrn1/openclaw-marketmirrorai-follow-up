import os

import json

import requests

from datetime import datetime, timezone



API_KEY = os.getenv("FINNHUB_API_KEY")



WATCHLIST = ["SPY", "QQQ", "NVDA", "GLD", "SLV", "USO", "XOM", "CVX", "BAC"]



snapshot = {

    "timestamp_utc": datetime.now(timezone.utc).isoformat(),

    "source": "Finnhub",

    "watchlist": {}

}



for symbol in WATCHLIST:

    url = "https://finnhub.io/api/v1/quote"

    params = {"symbol": symbol, "token": API_KEY}

    r = requests.get(url, params=params)

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

        "raw": data

    }



with open("data/market_snapshot.json", "w") as f:

    json.dump(snapshot, f, indent=2)



print("Saved: data/market_snapshot.json")

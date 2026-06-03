import json



with open("data/market_snapshot.json", "r") as f:

    snapshot = json.load(f)



watchlist = snapshot["watchlist"]



print("MarketMirrorAI Snapshot Analysis")

print("Source:", snapshot["source"])

print("Timestamp UTC:", snapshot["timestamp_utc"])

print("\nPrimary Thesis Assets:")



for symbol in ["SPY", "QQQ", "NVDA"]:

    data = watchlist[symbol]

    print(f"- {symbol}: {data['change_pct']}%")



print("\nSecondary Confirmation Assets:")



for symbol in ["GLD", "SLV", "USO", "XOM", "CVX", "BAC"]:

    data = watchlist[symbol]

    print(f"- {symbol}: {data['change_pct']}%")



print("\nInitial Observations:")



spy = watchlist["SPY"]["change_pct"]

qqq = watchlist["QQQ"]["change_pct"]

nvda = watchlist["NVDA"]["change_pct"]

gld = watchlist["GLD"]["change_pct"]

uso = watchlist["USO"]["change_pct"]

bac = watchlist["BAC"]["change_pct"]



if spy > 0 and qqq > 0 and nvda < 0:

    print("- Divergence: SPY and QQQ positive while NVDA is negative.")

    print("- Possible AI leadership weakness. Monitor closely.")



if gld > 1:

    print("- GLD is showing defensive strength above +1%.")

    print("- Possible safety/inflation/fear positioning.")



if uso < -1:

    print("- USO is weak below -1%.")

    print("- Energy complex may be under pressure.")



if bac > 1:

    print("- BAC is strong above +1%.")

    print("- Financials may be supporting market risk appetite.")



print("\nAlert Status:")



flags = 0



if spy > 0 and qqq > 0 and nvda < 0:

    flags += 1



if gld > 1:

    flags += 1



if uso < -1:

    flags += 1



if bac > 1:

    flags += 1



if flags >= 4:

    print("Level 3 — Early Warning")

elif flags >= 2:

    print("Level 2 — Increased Attention")

elif flags >= 1:

    print("Level 1 — Observation")

else:

    print("No alert. Continue monitoring.")



print("Flags detected:", flags)

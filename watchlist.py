import os

import requests



API_KEY = os.getenv("FINNHUB_API_KEY")



WATCHLIST = [

    "SPY",

    "QQQ",

    "NVDA",

    "GLD",

    "SLV",

    "USO",

    "XOM",

    "CVX",

    "BAC"

]



for symbol in WATCHLIST:



    url = "https://finnhub.io/api/v1/quote"



    params = {

        "symbol": symbol,

        "token": API_KEY

    }



    r = requests.get(url, params=params)



    data = r.json()



    print("\n======================")

    print(symbol)

    print("======================")



    print("Current:", data.get("c"))

    print("Open:", data.get("o"))

    print("High:", data.get("h"))

    print("Low:", data.get("l"))

    print("Previous Close:", data.get("pc"))

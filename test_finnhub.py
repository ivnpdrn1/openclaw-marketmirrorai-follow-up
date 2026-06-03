import os

import requests



api_key = os.getenv("FINNHUB_API_KEY")



symbol = "SPY"



url = "https://finnhub.io/api/v1/quote"



params = {

    "symbol": symbol,

    "token": api_key

}



response = requests.get(url, params=params)



print("Status:", response.status_code)

print("Response:")

print(response.json())

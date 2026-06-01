import requests

API_KEY = "YOUR_TWELVEDATA_API_KEY"

def get_candles(symbol="EUR/USD", interval="1min"):

    url = (
        f"https://api.twelvedata.com/time_series?"
        f"symbol={symbol}"
        f"&interval={interval}"
        f"&outputsize=100"
        f"&apikey={API_KEY}"
    )

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

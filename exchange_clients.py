import requests

class BinanceClient:
    BASE_URL = "https://api.binance.com/api/v3"

    def get_all_pairs(self):
        response = requests.get(f"{self.BASE_URL}/ticker/bookTicker")
        response.raise_for_status()
        pairs = response.json()
        return [(pair["symbol"], float(pair["bidPrice"]), float(pair["askPrice"])) for pair in pairs]


class BybitClient:
    BASE_URL = "https://api.bybit.com/v2/public"

    def get_all_pairs(self):
        response = requests.get(f"{self.BASE_URL}/tickers")
        response.raise_for_status()
        pairs = response.json()["result"]
        return [(pair["symbol"], float(pair["bid_price"]), float(pair["ask_price"])) for pair in pairs]


class BitgetClient:
    BASE_URL = "https://api.bitget.com/api/spot/v1"

    def get_all_pairs(self):
        response = requests.get(f"{self.BASE_URL}/market/tickers")
        response.raise_for_status()
        pairs = response.json()["data"]
        return [(pair["symbol"], float(pair["bestBid"]), float(pair["bestAsk"])) for pair in pairs]
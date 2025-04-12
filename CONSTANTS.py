from itertools import combinations_with_replacement

CREDENTIALS_FILE = 'creds.json'

ASSETS = [
    "UAH",
    "BTC",
    "USDT",
    "ETH"
]

combinations = list(combinations_with_replacement(ASSETS, 2))
ALL_ASSET_COUPLES = list(set(combinations + list(map(lambda x: x[::-1], combinations))))

BANKS_UA = {
    "PrivatBank": "ПриватБанк",
    "MonoBank": "МоноБанк"
}

OPERATION_TYPES = {
    "T+T": ("BUY", "SELL"),
    "M+M": ("SELL", "BUY"),
    "T+M": ("BUY", "BUY"),
    "M+T": ("SELL", "BUY")
}

SYMBOLS = [
    "ETHUAH",
    "BTCUAH",
    "USDTUAH",
    "BTCETH",
    "USDTBTC",
    "USDTETH"
]
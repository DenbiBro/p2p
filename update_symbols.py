from exchange_clients import BinanceClient, BybitClient, BitgetClient
from arbitrage_checker import check_arbitrage_opportunities

def update_symbols():
    binance = BinanceClient()
    bybit = BybitClient()
    bitget = BitgetClient()

    # Отримуємо всі пари з кожної біржі
    binance_pairs = binance.get_all_pairs()
    bybit_pairs = bybit.get_all_pairs()
    bitget_pairs = bitget.get_all_pairs()

    # Об'єднуємо всі пари
    all_pairs = binance_pairs + bybit_pairs + bitget_pairs

    # Перевіряємо можливості арбітражу
    arbitrage_pairs = check_arbitrage_opportunities(all_pairs)

    # Формуємо список пар для оновлення
    new_symbols = [pair[0] for pair in arbitrage_pairs]
    return new_symbols
from exchange_clients import BinanceClient, BybitClient, BitgetClient

def test_binance_client():
    binance = BinanceClient()
    pairs = binance.get_all_pairs()
    assert len(pairs) > 0, "Binance: Жодної пари не знайдено!"
    print("Binance Client Test Passed. Перші 5 пар:", pairs[:5])

def test_bybit_client():
    bybit = BybitClient()
    pairs = bybit.get_all_pairs()
    assert len(pairs) > 0, "Bybit: Жодної пари не знайдено!"
    print("Bybit Client Test Passed. Перші 5 пар:", pairs[:5])

def test_bitget_client():
    bitget = BitgetClient()
    pairs = bitget.get_all_pairs()
    assert len(pairs) > 0, "Bitget: Жодної пари не знайдено!"
    print("Bitget Client Test Passed. Перші 5 пар:", pairs[:5])

if __name__ == "__main__":
    test_binance_client()
    test_bybit_client()
    test_bitget_client()
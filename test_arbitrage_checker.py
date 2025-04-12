from arbitrage_checker import check_arbitrage_opportunities

def test_arbitrage_checker():
    test_pairs = [
        ("BTCUSDT", 30000, 29900),  # Є можливість арбітражу
        ("ETHUSDT", 2000, 2020),   # Немає можливості арбітражу
        ("BNBUSDT", 330, 320),     # Є можливість арбітражу
    ]
    arbitrage_pairs = check_arbitrage_opportunities(test_pairs)
    assert len(arbitrage_pairs) == 2, "Має бути знайдено 2 пари для арбітражу!"
    print("Arbitrage Checker Test Passed. Знайдені пари:", arbitrage_pairs)

if __name__ == "__main__":
    test_arbitrage_checker()
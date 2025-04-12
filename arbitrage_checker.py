def check_arbitrage_opportunities(pairs):
    """
    Перевіряє арбітражні можливості для валютних пар.
    :param pairs: список валютних пар у форматі (symbol, bid_price, ask_price)
    :return: список пар з можливостями арбітражу
    """
    arbitrage_pairs = []
    for symbol, bid_price, ask_price in pairs:
        # Якщо ціна продажу (bid) вища за ціну купівлі (ask), є можливість арбітражу
        if bid_price > ask_price:
            arbitrage_pairs.append((symbol, bid_price, ask_price))
    return arbitrage_pairs
from parsers import *
from CONSTANTS import BANKS_UA, ALL_ASSET_COUPLES, OPERATION_TYPES, SYMBOLS
import asyncio


def calculate_profit(bank_amount, from_asset_p2p, to_asset_p2p, exchange_price, ratio=1):
    amount_after_operation = (bank_amount / from_asset_p2p) * (exchange_price ** ratio) * to_asset_p2p

    return amount_after_operation - bank_amount


def get_user_url(user_id):
    url = "https://p2p.binance.com/uk/advertiserDetail?advertiserNo="

    return url + user_id


def make_total_data_array(fiat, bank_amount, limits):
    total_array = []
    all_params_array = []

    for symbol in SYMBOLS:
        all_params_array.append(form_symbol_price_params(symbol))

    for operation_type in OPERATION_TYPES:
        # Враховуємо тільки банки "ПриватБанк" та "МоноБанк"
        for bank in ["PrivatBank", "MonoBank"]:
            for asset_couple in ALL_ASSET_COUPLES:
                all_params_array += get_all_params(
                    *asset_couple, fiat, OPERATION_TYPES[operation_type], bank, limits
                )

    asyncio.run(load_data(all_params_array))
    all_data.sort(key=lambda s: s[0])

    for idx in range(len(all_data) // 2):
        from_asset = all_data[2 * idx][1]
        to_asset = all_data[2 * idx + 1][1]

        if from_asset["asset"] + to_asset["asset"] in SYMBOLS:
            cur_symbol = from_asset["asset"] + to_asset["asset"]
            ratio = 1
        else:
            cur_symbol = to_asset["asset"] + from_asset["asset"]
            ratio = -1
        analytics = get_analytics(bank_amount, from_asset, to_asset,
                                  calculate_profit(
                                      bank_amount,
                                      float(from_asset["price"]),
                                      float(to_asset["price"]),
                                      all_symbols_data[cur_symbol],
                                      ratio=ratio
                                  ),
                                  list(OPERATION_TYPES.keys())[idx // 64])
        total_array.append(analytics)

    return total_array


def get_all_params(from_asset, to_asset, fiat, order_type, bank, limits):
    from_asset_info = form_asset_info_params(from_asset, fiat, order_type[0], pay_types=[bank], limit=limits[order_type[0]])
    to_asset_info = form_asset_info_params(to_asset, fiat, order_type[1], pay_types=[bank], limit=limits[order_type[1]])

    return [from_asset_info, to_asset_info]


def get_analytics(bank_amount, from_info, to_info, profit, operation_type):
    formatted_info = [
        "Binance",
        operation_type,
        from_info["asset"],
        to_info["asset"],
        from_info["payment_system"],
        to_info["payment_system"],
        "",
        "",
        from_info["price"],
        to_info["price"],
        f'=HYPERLINK("{get_user_url(from_info["user_id"])}"; "{from_info["user_nickname"]}")',
        f'=HYPERLINK("{get_user_url(to_info["user_id"])}"; "{to_info["user_nickname"]}")',
        profit / bank_amount * 100,
        profit
    ]

    return formatted_info
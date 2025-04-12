from update_symbols import update_symbols
from CONSTANTS import SYMBOLS

def main():
    # Оновити список валютних пар
    updated_symbols = update_symbols()
    SYMBOLS.clear()
    SYMBOLS.extend(updated_symbols)

    # Запуск основного коду
    print("Оновлені пари для арбітражу:", SYMBOLS)
    # Вставити основну логіку роботи програми

if __name__ == "__main__":
    main()
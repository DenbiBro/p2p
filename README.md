# P2P Arbitrage Analyzer

## Встановлення
1. Клонувати репозиторій:
   ```bash
   git clone https://github.com/DenbiBro/p2p.git
   cd p2p
   ```

2. Створити віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```

3. Встановити залежності:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск GUI
1. Запустіть файл `gui.py`:
   ```bash
   python gui.py
   ```

## Створення `.exe`
1. Виконайте команду для створення `.exe`:
   ```bash
   pyinstaller --onefile --windowed gui.py
   ```

2. Готовий `.exe` з'явиться в папці `dist`.

## Запуск Telegram-бота
1. Запустіть файл `telegram_bot.py`:
   ```bash
   python telegram_bot.py
   ```

## Нотатки
- Для роботи Telegram-бота необхідно вказати токен у змінній `TELEGRAM_BOT_TOKEN`.
- Використовуйте файл `requirements.txt` для встановлення залежностей.
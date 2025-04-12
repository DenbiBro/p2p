from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from global_state import global_state
from update_symbols import update_symbols
from CONSTANTS import SYMBOLS
from threading import Thread
from logger import logger
import time

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Користувач запустив команду /start")
    await update.message.reply_text("Привіт! Я бот для арбітражу. Використовуйте /update для оновлення списку пар.")

async def update_pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        updated_symbols = update_symbols()
        SYMBOLS.clear()
        SYMBOLS.extend(updated_symbols)
        await update.message.reply_text(f"Оновлено. Нові пари: {', '.join(SYMBOLS)}")
        logger.info("Список валютних пар оновлено через Telegram-бота")
    except Exception as e:
        await update.message.reply_text("Помилка при оновленні пар!")
        logger.error(f"Помилка при оновленні пар через Telegram-бота: {e}")

async def start_program(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not global_state.get_running():
        global_state.set_running(True)
        Thread(target=run_logic).start()
        await update.message.reply_text("Програма запущена!")
        logger.info("Програма запущена через Telegram-бота")
    else:
        await update.message.reply_text("Програма вже працює.")

async def stop_program(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if global_state.get_running():
        global_state.set_running(False)
        await update.message.reply_text("Програма зупинена!")
        logger.info("Програма зупинена через Telegram-бота")
    else:
        await update.message.reply_text("Програма вже зупинена.")

def run_logic():
    try:
        while global_state.get_running():
            logger.info("Основна логіка працює...")
            time.sleep(5)
    except Exception as e:
        logger.error(f"Помилка в основній логіці через Telegram-бота: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_API_KEY").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("update", update_pairs))
    app.add_handler(CommandHandler("start_program", start_program))
    app.add_handler(CommandHandler("stop_program", stop_program))

    app.run_polling()
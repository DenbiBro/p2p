import logging

# Налаштування логування
logging.basicConfig(
    filename='arbitrage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()

# Приклад використання
if __name__ == "__main__":
    logger.info("Програма запущена")
    logger.error("Це приклад помилки")
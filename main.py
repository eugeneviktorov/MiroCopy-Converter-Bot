import asyncio
import configparser
from aiogram import Bot, Dispatcher
from systems.client import router as client_router
from utils.logger import logger


config = configparser.ConfigParser()
config.read("config.ini")
BOT_TOKEN = config.get("token", "bot")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Запускаемая функция бота
async def main():
    dp.include_router(client_router)
    logger.info("🔄 Бот запускается...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"❌ Ошибка при старте polling: {e}")


# Запуск системы бота
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен пользователем")

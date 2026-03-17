import asyncio
import os
from aiogram import Bot, Dispatcher
from handler import router, init_db
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    # 1. Сначала создаем таблицы в БД
    print("Инициализация базы данных...")
    await init_db()

    # 2. Создаем объекты бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("Бот запущен и готов к работе!")

    # 3. Запускаем опрос серверов Telegram
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
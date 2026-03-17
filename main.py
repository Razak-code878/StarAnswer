import asyncio
import os
from aiogram import Bot, Dispatcher
from handler import router, init_db  # init_db уже импортирован, это отлично
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    # 1. Сначала инициализируем БД
    print("Проверка базы данных...")
    await init_db()

    # 2. Инициализируем бота и диспетчер внутри main
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("Бот успешно запущен!")

    # 3. Запускаем получение обновлений
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
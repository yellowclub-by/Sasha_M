import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7189697687:AAGB9yCldmyNwYbf3wsCp8Ed0IzOnnQfISk"
bot = Bot(token=TOKEN)

dp = Dispatcher()
from handlers.user_privat import user_router
from handlers.user_group import group_router

dp.include_router(user_router)
dp.include_router(group_router)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7189697687:AAGB9yCldmyNwYbf3wsCp8Ed0IzOnnQfISk"
bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет, это бот по продаже ключей стим")


@dp.message()
async def echo(message: types.Message):
    await message.answer('Бот находится в разработке')
    user_text = message.text
    await message.answer(user_text)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())

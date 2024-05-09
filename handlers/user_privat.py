from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет, это бот по продаже ключей стим")


@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Вот наш каталог:')


@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("О нас:")


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакты:")


@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer("Филиалы:")


@user_router.message()
async def echo(message: types.Message):
    await message.answer('Бот находится в разработке')
    user_text = message.text
    await message.answer(user_text)

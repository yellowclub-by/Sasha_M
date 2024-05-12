from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет, это бот по продаже ключей стим")


@user_router.message(F.text.lower() == "каталог")
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Вот наш каталог:')


@user_router.message(F.text.lower() == "о нас")
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("О нас:")


@user_router.message(F.text.lower() == "контакты")
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакты:")


@user_router.message(F.text.lower() == "филиалы")
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer("Филиалы:")

# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == "доставка")
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.endswith("?"))
# @user_router.message(F.text.lower().startswith("как"), F.text.endswith('?'))
# @user_router.message((F.text.lower().contains("стоимост")) | (F.text.lower().contains("цен")))
# async def echo(message: types.Message):
#     await message.answer("Сработал магический фильтр")

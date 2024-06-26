from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    text = '''<strong>Добро пожаловать в наш бот для продажи ключей от игр!</strong>👋 \n
У нас вы найдете самые популярные и новейшие игры по выгодным ценам.🤑 Мы гарантируем быструю доставку ключей и отличное обслуживание.😍
Не упустите возможность погрузиться в увлекательные миры игр уже сегодня!💫 Оставайтесь с нами и будьте в курсе всех новинок и акций.😊
\n <b>Спасибо, что выбрали нас!</b>❤️'''
    await message.answer(text, reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == "каталог😎")
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer('Вот наш каталог:', reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == "о нас🦃")
@user_router.message(Command('about'))
async def about(message: types.Message):
    text = '''<strong>Keys Store - это телеграм-бот для продажи лицензионных ключей от компьютерных игр.🤩</strong>\n
Бот предлагает широкий выбор игр на различных платформах🎮. Пользователи могут искать, выбирать и покупать игровые ключи внутри бота.🤯\n
<i>Оплата осуществляется различными способами, включая банковские карты и электронные платежные системы💳.</i> <b>Бот также предоставляет поддержку пользователей 24/7.</b>⏲️'''
    await message.answer(text)


@user_router.message(F.text.lower() == "контакты🔔")
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    text = '<strong>Для связи с телеграм-ботом Keys Store по продаже ключей от игр, вы можете воспользоваться следующим контактом: @NE_ABABUS.</strong>😎'
    await message.answer(text)


@user_router.message(F.text.lower() == "филиалы🎐")
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer("ООН Савелий Огурчиков", reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.startswith('address'))
async def addresses_type(callback: types.CallbackQuery):
    quare = callback.data.split('_')[1]
    if quare == '1':
        await callback.message.answer("Rue des États-Unis")
    elif quare == '2':
        await callback.message.answer("Weiermattweg 32")
    elif quare == '3':
        await callback.message.answer("Rosenweg 27")
    elif quare == '4':
        await callback.message.answer("C. de María Nistal, 2-4")
    await callback.answer()


@user_router.message(F.text.lower() == "назад🔙")
async def back(message: types.Message):
    await message.answer('<b>Главное меню</b>', reply_markup=reply.start_kb)

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

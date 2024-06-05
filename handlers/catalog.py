from aiogram import F, Router, types
from aiogram.types import FSInputFile


catalog_router = Router()


@catalog_router.message(F.text.lower() == 'steam❤️')
async def catalog_st(message: types.Message):
    photo = FSInputFile(r'img\catalog\steam.jpg')
    text = '<b>Стоимость ключей от 50р</b>😎'
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'egs💫')
async def catalog_egs(message: types.Message):
    photo = FSInputFile(r'img\catalog\egs.jpg')
    text = '<b>Стоимость ключей от 100р</b>😊'
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'ubisoft😂')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ubi.jpg')
    text = '<b>Стоимость ключей от 300р</b>🤑'
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'ea🙌')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ea.png')
    text = '<b>Стоимость ключей от 200р</b>😍'
    await message.answer_photo(photo, caption=text)

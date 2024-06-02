from aiogram import F, Router, types
from aiogram.types import FSInputFile


catalog_router = Router()


@catalog_router.message(F.text.lower() == 'steam')
async def catalog_st(message: types.Message):
    photo = FSInputFile(r'img\catalog\steam.jpg')
    await message.answer_photo(photo, caption='Стоимость ключей от 50р')


@catalog_router.message(F.text.lower() == 'egs')
async def catalog_egs(message: types.Message):
    photo = FSInputFile(r'img\catalog\egs.jpg')
    await message.answer_photo(photo, caption='Стоимость ключей от 100р')


@catalog_router.message(F.text.lower() == 'ubisoft')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ubi.jpg')
    await message.answer_photo(photo, caption='Стоимость ключей от 300р')


@catalog_router.message(F.text.lower() == 'ea')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ea.png')
    await message.answer_photo(photo, caption='Стоимость ключей от 200р')

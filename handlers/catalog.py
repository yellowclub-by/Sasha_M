from aiogram import F, Router, types
from aiogram.types import FSInputFile


catalog_router = Router()


@catalog_router.message(F.text.lower() == 'steam❤️')
async def catalog_st(message: types.Message):
    photo = FSInputFile(r'img\catalog\steam.jpg')
    text = '''<strong>Keys Store предлагает доступные ключи от игр на платформе Steam по выгодным ценам.</strong>\n
Вы можете приобрести лицензионные ключи от различных игр. Будь то популярные хиты или скрытые жемчужины, Keys Store обеспечивает доступность и разнообразие выбора.😎\n
<b>Стоимость ключей начинается от 50 р.🤯</b>'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'egs💫')
async def catalog_egs(message: types.Message):
    photo = FSInputFile(r'img\catalog\egs.jpg')
    text = '''<b>Keys Store предлагает доступные ключи от игр на платформе Epic Games, начиная от 100 рублей</b>.🫢
Обновляйте свою коллекцию игр без больших затрат.😊'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'ubisoft😂')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ubi.jpg')
    text = '''<b>Keys Store предлагает лицензионные ключи от игр на платформе Ubisoft Connect, начиная от 300 рублей.</b>😎
Разнообразьте свою игровую библиотеку с захватывающими играми от Ubisoft по доступной цене.🤑'''
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'ea🙌')
async def catalog_ubi(message: types.Message):
    photo = FSInputFile(r'img\catalog\ea.png')
    text = '''<b>Keys Store предлагает лицензионные ключи от игр Electronic Arts по доступной цене, начиная от 200 рублей</b>.🤑
Получите доступ к захватывающим играм от EA без высоких затрат.😍'''
    await message.answer_photo(photo, caption=text)

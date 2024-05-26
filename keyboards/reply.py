from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='Про нас'),
        ],
        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='Филиалы')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Мяу'

)
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Steam'),
            KeyboardButton(text='EGS')
        ],
        [
            KeyboardButton(text='Ubisoft'),
            KeyboardButton(text='EA')
        ]
    ], resize_keyboard=True

)

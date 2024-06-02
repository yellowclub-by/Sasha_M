from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text="Назад")

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
        ],
        [
            back_btn
        ]
    ], resize_keyboard=True

)

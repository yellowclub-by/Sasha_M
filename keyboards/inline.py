from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Rue des États-Unis', callback_data='address_1'),
        InlineKeyboardButton(text="Weiermattweg 32", callback_data='address_2'),
        InlineKeyboardButton(text="Rosenweg 27", callback_data='address_3'),
        InlineKeyboardButton(text='C. de María Nistal, 2-4', callback_data='address_4'),
        width=2
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=asteriasanarchy')
        ]
    ]
)

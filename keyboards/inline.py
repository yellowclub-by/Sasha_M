from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Адрес 1', callback_data='address_1'),
        InlineKeyboardButton(text="Адрес 2", callback_data='address_2'),
        InlineKeyboardButton(text="Адрес 3", callback_data='address_3'),
        InlineKeyboardButton(text='Адрес 4', callback_data='address_4'),
        width=2
    )
    return builder.as_markup()

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext


def hello_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🇬🇧 English", callback_data="language:en")
    keyboard.button(text="🇷🇺 Русский", callback_data="language:ru")
    keyboard.adjust(1)
    return keyboard.as_markup()
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from aiogram_i18n import I18nContext
from utils.config import is_admin, hello_message
from utils.database import get_data, update_data
from files.keyboards import hello_keyboard

router = Router()

@router.message(Command("start"))
async def start_command(message: Message, i18n: I18nContext):
    user = message.from_user
    if i18n.locale == "":
        await message.answer(hello_message, reply_markup=hello_keyboard())
        return
    if is_admin(user.id):
        pass # later

# Test commands (dev only)

@router.message(Command("clear_state"))
async def test1_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Success!")
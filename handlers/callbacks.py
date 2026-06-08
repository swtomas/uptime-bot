from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

router = Router()

@router.callback_query(F.data.startswith("language:"))
async def language_callback(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    language = callback.data.split(":")[1]
    print(language)
    await state.update_data(language=language)
    i18n.locale = language
    await callback.answer(i18n.get("Alert_LanguageSelected"), show_alert=True)
    await callback.message.delete()
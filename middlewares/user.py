from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.fsm.context import FSMContext

async def get_language(state: FSMContext):
    data = await state.get_data()
    language = data.get('language')
    if not language:
      return ""
    return language

class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        i18n = data.get("i18n")
        state = data.get("state")
        if state:
            i18n.locale = await get_language(state)
        return await handler(event, data)
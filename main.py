from aiogram import Dispatcher
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores.fluent_runtime_core import FluentRuntimeCore
from aiogram.fsm.storage.redis import RedisStorage
from utils.config import bot, redis_client
from handlers.commands import router as commands_router
from handlers.callbacks import router as callbacks_router
from middlewares.user import UserMiddleware
import asyncio
import logging

async def main():
    storage = RedisStorage(redis_client)
    dp = Dispatcher(storage=storage)
    i18n = I18nMiddleware(
        core=FluentRuntimeCore(path="files/locales/{locale}")
    )
    i18n.setup(dispatcher=dp)

    dp.include_router(commands_router)
    dp.include_router(callbacks_router)

    dp.update.outer_middleware(UserMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
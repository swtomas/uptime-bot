from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import Bot
from redis.asyncio import Redis

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN: int
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USERNAME: str
    REDIS_PASSWORD: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

config = Settings()
bot = Bot(token=config.BOT_TOKEN)
redis_client = Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            username=config.REDIS_USERNAME,
            password=config.REDIS_PASSWORD,
            decode_responses=True
        )
hello_message = """
🇬🇧: Please, select your language
🇷🇺: Пожалуйста, выберите ваш язык
"""

def is_admin(user_id: int) -> bool:
    return user_id == config.ADMIN


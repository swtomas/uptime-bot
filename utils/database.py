from utils.config import redis_client

async def get_data(key: str) -> str | int | bool:
    try:
        data = await redis_client.get(key)
        return data
    except Exception:
        return False

async def update_data(key: str, data: str | int) -> bool:
    try:
        await redis_client.set(key, data)
        return True
    except Exception:
        return False
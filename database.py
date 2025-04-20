import asyncio
from models.base import Base
from core.session import *


# Clear all metadata and recreate tables
async def reset_metadata():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drop all tables
        await conn.run_sync(Base.metadata.create_all)  # Recreate all tables


if __name__ == "__main__":
    asyncio.run(reset_metadata())
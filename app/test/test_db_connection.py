import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.session import AsyncSessionLocal

async def test_db():
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        print("Connected:", result.scalar())


if __name__ == "__main__":
    asyncio.run(test_db())
    
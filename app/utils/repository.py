from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC):
    @abstractmethod
    async def create(self, item):
        pass

    @abstractmethod
    async def read(self, item_id):
        pass

    @abstractmethod
    async def update(self, item_id, item):
        pass

    @abstractmethod
    async def delete(self, item_id) -> bool:
        pass

    @abstractmethod
    async def list(self):
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> Optional[T]:
        pass

class SQLRepository(Repository):
    def __init__(self, session: AsyncSession, model):
        self.session = session
        self.model = model
        if model is None:
            raise ValueError("Model cannot be None")
        print(f'{T.__name__}, {T}')

    async def create(self, item):
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def read(self, item_id):
        result = await self.session.execute(select(T).filter_by(id=item_id))
        return result.scalars().first()

    async def update(self, item_id, item):
        existing_item = await self.read(item_id)
        if existing_item:
            for key, value in item.__dict__.items():
                setattr(existing_item, key, value)
            await self.session.commit()
            return existing_item
        return None

    async def delete(self, item_id) -> bool:
        item = await self.read(item_id)
        if item:
            await self.session.delete(item)
            await self.session.commit()
            return True
        return False

    async def list(self) -> List:
        result = await self.session.execute(select(T))
        return result.scalars().all()
    
    async def get_by_name(self, name: str):
        print(f"get_by_name: {name}")
        result = await self.session.execute(select(self.model).filter_by(username=name))
        return result.scalars().first()
    
    async def check(self, key, value):
        result = await self.session.execute(select(self.model).filter_by(**{key: value}))
        return result.scalars().first()
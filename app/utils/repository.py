from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm.util import has_identity

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
    async def update(self, item_id, item, existing_item=None):
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
        try:
            result = await self.session.execute(select(self.model).filter_by(id=item_id))
        except Exception as e:
            print(f"Error executing query: {e}")
            raise e
        return result.scalars().first()

    async def update(self, item_id, item, existing_item=None):
        print("existing_item",existing_item)
        if existing_item is None:
            existing_item = await self.read(item_id)
        print(item.__dict__)
        print(existing_item.__dict__)
        if existing_item:
            for key, value in item.__dict__.items():
                try:
                    setattr(existing_item, key, value)
                    
                except AttributeError:
                    print(f"Attribute {key} not found in {self.model.__name__}")
            try:
                print(f"Updating item: {has_identity(existing_item)}")
                await self.session.commit()
            except Exception as e:
                await self.session.rollback()
                raise e
            return existing_item
        return None

    async def delete(self, item_id) -> bool:
        item = await self.read(item_id)
        if item:
            await self.session.delete(item)
            await self.session.commit()
            return True
        return False

    async def list(self):
        result = await self.session.execute(select(self.model))
        if result is None:
            return []
        return result.scalars().all()
    
    async def get_by_name(self, name: str):
        print(f"get_by_name: {name}")
        result = await self.session.execute(select(self.model).filter_by(username=name))
        return result.scalars().first()
    
    async def check(self, key, value):
        result = await self.session.execute(select(self.model).filter_by(**{key: value}))
        return result.scalars().first()
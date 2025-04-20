from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.utils.repository import Repository, SQLRepository
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, user_repository : Repository):
        self.user_repository = user_repository

    async def create_user(self, user_data):
        # Validate and create a new user
        return await self.user_repository.create(user_data)

    async def get_user(self, user_id):
        # Retrieve user by ID
        return await self.user_repository.read(user_id)

    async def update_user(self, user_id, user_data, existing_user = None):
        # Update existing user
        return await self.user_repository.update(user_id, user_data, existing_user)

    async def delete_user(self, user_id):
        # Delete a user
        return await self.user_repository.delete(user_id)
    
    async def list_users(self):
        # List all users
        return await self.user_repository.list()
    

class UserCreateService(UserService):
    def __init__(self, session : AsyncSession):
        self.user_repository = SQLRepository(session, User)
        super().__init__(self.user_repository)
    
    async def create(self, user_data : UserCreate) -> UserRead:
        
        # Validate and create a new user
        if user_data.password != user_data.password_repeat:
            raise ValueError("Passwords do not match")
        print(user_data.username, user_data.password, user_data.password_repeat)
        exist_user = await self.user_repository.check('username',user_data.username)
        exist_user_email = await self.user_repository.check('email',user_data.email)
        if exist_user_email:
            raise ValueError("Email already exists")
        if exist_user:
            raise ValueError("Username already exists")
        
        user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )
        result = await self.create_user(user)
        return UserRead.model_validate(result)
    
class UserUpdateService(UserService):
    def __init__(self, session : AsyncSession):
        self.user_repository = SQLRepository(session, User)
        super().__init__(self.user_repository)

    async def update(self, user_id : int, user_data : UserUpdate) -> UserRead:
        # Validate and update an existing user
        if user_id != user_data.id:
            raise ValueError("User ID mismatch")
        data = User(
            username=user_data.username,
            email=user_data.email
        )
        exist_user = await self.user_repository.read(user_id)
        user = await self.update_user(user_id, data, exist_user)
        if not user:
            raise ValueError("User not found")
        
        return UserRead.model_validate(user)
    
class UserReadService(UserService):
    def __init__(self, session : AsyncSession):
        self.user_repository = SQLRepository(session, User)
        super().__init__(self.user_repository)

    async def read(self, user_id : int) -> UserRead:
        # Validate and update an existing user
        user = await self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        return UserRead.model_validate(user)
    
    async def list_users(self):
        # Validate and update an existing user
        users = await self.list_users()
        if not users:
            raise ValueError("Users not found")
        
        return [UserRead.model_validate(user) for user in users]
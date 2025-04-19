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

    def get_user(self, user_id):
        # Retrieve user by ID
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id, user_data):
        # Update existing user
        return self.user_repository.update(user_id, user_data)

    def delete_user(self, user_id):
        # Delete a user
        return self.user_repository.delete(user_id)
    
    

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
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        return UserRead.model_validate(user)
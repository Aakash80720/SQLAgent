from typing import Optional
from pydantic import BaseModel, EmailStr, Field, model_validator

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)
    password_repeat: str = Field(..., min_length=8, max_length=128)
    is_active: Optional[bool] = True


class UserRead(UserBase):
    id: int
    is_active: bool = True

    model_config = {
        "from_attributes" : True,
    }

    
class UserUpdate(UserBase):
    pass

class UserDelete(BaseModel):
    id: int = Field(..., gt=0)
    is_active: Optional[bool] = False
import uuid
from uuid import UUID

from typing import Optional, Union
from pydantic import BaseModel, Field
class UserRequestModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: list

class UserResponseModel(UserRequestModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: list

class User(UserRequestModel):
    user_id: UUID


userList = [
    User(
        user_id=uuid.uuid4(),
        first_name="Rodrigo",
        last_name="Gallego",
        email="test@gmail.com",
        years_previous_experience=5,
        skills= [
            {"Python": 1},
            {"NoSQL": 2}
        ]
    ),
    User(
        user_id=uuid.uuid4(),
        first_name="Andrés",
        last_name="Gallego",
        email="test2@gmail.com",
        years_previous_experience=1,
        skills= [
            {"Python": 1},
            {"NoSQL": 2}
        ]
    )
]
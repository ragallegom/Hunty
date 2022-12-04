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
    vacancies_available: list

class User(UserRequestModel):
    user_id: UUID


userList = [
    User(
        user_id='fd3512a1-2a18-4473-992d-31b5d522ecf7',
        first_name="Rodrigo",
        last_name="Gallego",
        email="test@gmail.com",
        years_previous_experience=5,
        skills= [
            {"Python": 5},
            {"NoSQL": 4},
            {"AWS": 3},
            {"Angular": 6}
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
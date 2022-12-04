from typing import Optional
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: list

class UserResponseModel(UserRequestModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: list

userList = [
    UserRequestModel(
        user_id=1,
        first_name="Rodrigo",
        last_name="Gallego",
        email="test@gmail.com",
        years_previous_experience=5,
        skills= [
            {"Python": 1},
            {"NoSQL": 2}
        ]
    ),
    UserRequestModel(
        user_id=2,
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
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
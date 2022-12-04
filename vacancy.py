import uuid
from uuid import UUID

from typing import Optional, Union
from pydantic import BaseModel

class VacancyRequestModel(BaseModel):
    position_name: str
    company_name: str
    salary: int
    currency: str
    vacancy_link: str
    required_skills: list
 
class VacancyResponseModel(VacancyRequestModel):
    position_name: str
    company_name: str
    salary: int
    currency: str
    vacancy_link: str
    required_skills: list

    vacancy_id: UUID

class Vacancy(VacancyRequestModel):
    vacancy_id: UUID


vacanciesList = [
    Vacancy(
        vacancy_id= uuid.uuid4(),
        position_name= "Python Dev",
        company_name= "Test Company",
        salary= 9999999,
        currency= "COP",
        vacancy_link= "https://www.test.com",
        required_skills= [
            {"Python" : 3},
            {"NoSQL" : 5},
            {"AWS": 2}
        ]
    ),
    Vacancy(
        vacancy_id= uuid.uuid4(),
        position_name= "Angular Dev",
        company_name= "Test 2 Company",
        salary= 9999999,
        currency= "COP",
        vacancy_link= "https://www.test2.com",
        required_skills= [
            {"Angular" : 3},
            {"NoSQL" : 2},
            {"AWS": 5}
        ]
    )
]
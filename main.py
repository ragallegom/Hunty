import uuid

from fastapi import FastAPI, HTTPException
from user import UserRequestModel, UserResponseModel, User, userList
from vacancy import VacancyRequestModel, VacancyResponseModel, Vacancy, vacanciesList

users = userList
vacancies = vacanciesList

app = FastAPI(
    title='Hunty',
    description='Prueba Tecnica',
    version='1.0.1'
)


@app.get('/')
async def index():
    return {"message": "Prueba técnica Hunty"}


"""
    User CRUD
"""
@app.post('/users')
async def create_user(user_request: UserRequestModel):
    user = User(
        user_id=uuid.uuid4(),
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        email=user_request.email,
        years_previous_experience=user_request.years_previous_experience,
        skills=user_request.skills
    )

    users.append(user)

    return user

@app.get('/users')
async def get_all_user():

    if users:
        return users
    else:
        return HTTPException(404, "We don't have user")

@app.get('/users/{user_id}')
async def get_user(user_id):

    user = next((user for user in users if user.user_id == uuid.UUID(user_id)), None)
    vacancies_available= []
    
    if user:
        for vacancy in vacancies:
            length_skills = len(vacancy.required_skills)
            user_skills = set().union(*(d.keys() for d in user.skills))
            passed_skills = 0

            for skill in user_skills:
                val_req = [d[skill] for d in vacancy.required_skills if skill in d]
                val_user = [d[skill] for d in user.skills if skill in d]

                if val_user and val_req and val_user >= val_req:
                    passed_skills+=1 

            accepted_average = (passed_skills/length_skills)*100

            if(accepted_average >= 50):
                vacancies_available.append(vacancy)
            
        return UserResponseModel(
            user_id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            years_previous_experience=user.years_previous_experience,
            skills=user.skills,
            vacancies_available=vacancies_available
        )
    else:
        return HTTPException(404, 'User not found')

@app.delete('/users/{user_id}')
async def remove_user(user_id):

    user = next((user for user in users if user.user_id == uuid.UUID(user_id)), None)
    
    if user:
        users.remove(user)
        return True
    else:
        return HTTPException(404, 'User not found')

@app.put('/users/{user_id}')
async def update_user(user_id, user_request: UserRequestModel):         
    old_user = next((user for user in users if user.user_id == uuid.UUID(user_id)), None)
    
    if old_user:
        if user_request:
            update_user = User(
                user_id=uuid.UUID(user_id),
                first_name=user_request.first_name,
                last_name=user_request.last_name,
                email=user_request.email,
                years_previous_experience=user_request.years_previous_experience,
                skills=user_request.skills
            )

            for idx, user in enumerate(users):
                if old_user in user:
                    users[idx] = update_user
            
            return update_user

        else: 
            return HTTPException(400, 'Without information')

    else:
        return HTTPException(404, 'User not found')

"""
    Vancacy CRUD
"""
@app.post('/vacancies')
async def create_vacancy(vacancy_request: VacancyRequestModel):
    vacancy = Vacancy(
        vacancy_id= uuid.uuid4(),
        position_name=vacancy_request.position_name,
        company_name=vacancy_request.company_name,
        salary=vacancy_request.salary,
        currency=vacancy_request.currency,
        vacancy_link=vacancy_request.vacancy_link,
        required_skills=vacancy_request.required_skills
    )

    vacancies.append(vacancy)

    return vacancy

@app.get('/vacancies')
async def get_all_vacancies():

    if vacancies:
        return vacancies
    else:
        return HTTPException(404, "We don't have vacancies")

@app.get('/vacancies/{vacancy_id}')
async def get_vacancy(vacancy_id):

    vacancy = next((vacancy for vacancy in vacancies if vacancy.vacancy_id == uuid.UUID(vacancy_id)), None)

    if vacancy:
        return VacancyResponseModel(
            vacancy_id=vacancy.vacancy_id,
            position_name=vacancy.position_name,
            company_name=vacancy.company_name,
            salary=vacancy.salary,
            currency=vacancy.currency,
            vacancy_link=vacancy.vacancy_link,
            required_skills=vacancy.required_skills
        )
    else:
        return HTTPException(404, 'Vacancy not found')

@app.delete('/vacancies/{vacancy_id}')
async def remove_vacancy(vacancy_id):

    vacancy = next((vacancy for vacancy in vacancies if vacancy.vacancy_id == uuid.UUID(vacancy_id)), None)
    
    if vacancy:
        vacancies.remove(vacancy)
        return True
    else:
        return HTTPException(404, 'Vacancy not found')

@app.put('/vacancies/{vacancy_id}')
async def update_vacancy(vacancy_id, vacancy_request: VacancyRequestModel):         
    old_vacancy = next((vacancy for vacancy in vacancies if vacancy.vacancy_id == uuid.UUID(vacancy_id)), None)
    
    if old_vacancy:
        if vacancy_request:
            update_vacancy = Vacancy(
                vacancy_id= uuid.UUID(vacancy_id),
                position_name=vacancy_request.position_name,
                company_name=vacancy_request.company_name,
                salary=vacancy_request.salary,
                currency=vacancy_request.currency,
                vacancy_link=vacancy_request.vacancy_link,
                required_skills=vacancy_request.required_skills
            )

            for idx, vacancy in enumerate(vacancies):
                if old_vacancy in vacancy:
                    vacancies[idx] = update_vacancy
            
            return update_vacancy

        else: 
            return HTTPException(400, 'Without information')

    else:
        return HTTPException(404, 'Vacancy not found')

"""
    Company R
"""
@app.get('/companies')
async def get_all_companies():

    companiesList = []
    if vacancies:
        for vacancy in vacancies:
            if vacancy.company_name not in companiesList:
                companiesList.append(vacancy.company_name)
        return companiesList
    else:
        return HTTPException(404, "We don't have companies")
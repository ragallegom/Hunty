import json 
import uuid

from fastapi.testclient import TestClient
from user import User, userList
from vacancy import Vacancy, vacanciesList

from main import app

"""
    Unit Test
"""

client = TestClient(app)

def test_read_index():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Prueba técnica Hunty"}


"""
    User Test
"""

def test_get_all_users():
    response = client.get("/users")
    assertUserList = []
    for user in response.json():
        assertUserList.append(
            User(
                user_id=user['user_id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                years_previous_experience=user['years_previous_experience'],
                skills=user['skills']
            )
        )
    assert assertUserList == userList

def test_get_user_success():
    id_test = userList[0].user_id
    response = client.get("/users/"+str(id_test))
    user = response.json()

    user_test = User(
        user_id=user['user_id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        email=user['email'],
        years_previous_experience=user['years_previous_experience'],
        skills=user['skills']
    )

    assert user_test == userList[0]

def test_get_user_fail():
    id_test = uuid.uuid4()
    response = client.get("/users/"+str(id_test))


    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'User not found'

def test_create_user_success():
    json_user = {
            "first_name": "test",
            "last_name": "hunty",
            "email": "test@gmail.com",
            "years_previous_experience": 2,
            "skills": [
                {"Python": 2}
            ]
        }
    response = client.post(
        "/users",
        json=json_user
    )

    assert response.json()['first_name'] == json_user['first_name']

def test_create_user_fail():
    json_user = {
            "last_name": "hunty",
            "email": "test@gmail.com",
            "years_previous_experience": 2,
            "skills": [
                {"Python": 2}
            ]
        }
    response = client.post(
        "/users",
        json=json_user
    )

    assert response.status_code == 422

def test_remove_user_success():
    id_test = userList[0].user_id
    response = client.delete("/users/"+str(id_test))

    assert response.status_code == 200
    assert response.json() == True

def test_remove_user_fail():
    id_test = uuid.uuid4()
    response = client.delete("/users/"+str(id_test))

    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'User not found'

def test_update_user_success():
    id_test = userList[0].user_id
    json_user = {
            "first_name": "test",
            "last_name": "hunty",
            "email": "test@gmail.com",
            "years_previous_experience": 2,
            "skills": [
                {"Python": 2}
            ]
        }
    response = client.put(
        "/users/"+str(id_test),
        json=json_user
    )

    assert userList[0].user_id == uuid.UUID(response.json()['user_id'])
    assert userList[0].first_name != response.json()['first_name']
    assert response.json()['first_name'] == json_user['first_name']

def test_update_user_fail_without_information():
    id_test = userList[0].user_id
    json_user = {
            "last_name": "hunty",
            "email": "test@gmail.com",
            "years_previous_experience": 2,
            "skills": [
                {"Python": 2}
            ]
        }
    response = client.put(
        "/users/"+str(id_test),
        json=json_user
    )

    assert response.status_code == 422

def test_update_user_fail_user_not_found():
    id_test = uuid.uuid4()
    json_user = {
            "first_name": "test",
            "last_name": "hunty",
            "email": "test@gmail.com",
            "years_previous_experience": 2,
            "skills": [
                {"Python": 2}
            ]
        }
    response = client.put(
        "/users/"+str(id_test),
        json=json_user
    )

    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'User not found'

"""
    Vacancy Test
"""

def test_get_all_vacancies():
    response = client.get("/vacancies")
    assertList = []
    for vacancy in response.json():
        assertList.append(
            Vacancy(
                vacancy_id=vacancy['vacancy_id'],
                position_name=vacancy['position_name'],
                company_name=vacancy['company_name'],
                salary=vacancy['salary'],
                currency=vacancy['currency'],
                vacancy_link=vacancy['vacancy_link'],
                required_skills=vacancy['required_skills']
            )
        )
    assert assertList == vacanciesList

def test_get_vacancy_success():
    id_test = vacanciesList[0].vacancy_id
    response = client.get("/vacancies/"+str(id_test))
    vacancy = response.json()

    vacancy_test = Vacancy(
                vacancy_id=vacancy['vacancy_id'],
                position_name=vacancy['position_name'],
                company_name=vacancy['company_name'],
                salary=vacancy['salary'],
                currency=vacancy['currency'],
                vacancy_link=vacancy['vacancy_link'],
                required_skills=vacancy['required_skills']
            )

    assert vacancy_test == vacanciesList[0]

def test_get_vacancy_fail():
    id_test = uuid.uuid4()
    response = client.get("/vacancies/"+str(id_test))


    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'Vacancy not found'

def test_create_vacancy_success():
    json_vacancy = {
            "position_name": "Python Dev",
            "company_name": "Test Company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_link": "https://www.test.com",
            "required_skills":[
                {"Python" : 3},
                {"NoSQL" : 2}
            ]
        }
    response = client.post(
        "/vacancies",
        json=json_vacancy
    )
    print(response)
    assert response.json()['position_name'] == json_vacancy['position_name']

def test_create_vacancy_fail():
    json_vacancy = {
            "company_name": "Test Company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_link": "https://www.test.com",
            "required_skills":[
                {"Python" : 3},
                {"NoSQL" : 2}
            ]
        }
    response = client.post(
        "/vacancies",
        json=json_vacancy
    )

    assert response.status_code == 422

def test_remove_vacancy_success():
    id_test = vacanciesList[0].vacancy_id
    response = client.delete("/vacancies/"+str(id_test))

    assert response.status_code == 200
    assert response.json() == True

def test_remove_vacancy_fail():
    id_test = uuid.uuid4()
    response = client.delete("/vacancies/"+str(id_test))

    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'Vacancy not found'

def test_update_vacancy_success():
    id_test = vacanciesList[0].vacancy_id
    json_vacancy = {
            "position_name": "Python Senior Dev",
            "company_name": "Test Company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_link": "https://www.test.com",
            "required_skills":[
                {"Python" : 3},
                {"NoSQL" : 2}
            ]
        }
    response = client.put(
        "/vacancies/"+str(id_test),
        json=json_vacancy
    )

    assert vacanciesList[0].vacancy_id == uuid.UUID(response.json()['vacancy_id'])
    assert vacanciesList[0].position_name != response.json()['position_name']
    assert response.json()['position_name'] == json_vacancy['position_name']

def test_update_vacancy_fail_without_information():
    id_test = vacanciesList[0].vacancy_id
    json_vacancy = {
            "company_name": "Test Company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_link": "https://www.test.com",
            "required_skills":[
                {"Python" : 3},
                {"NoSQL" : 2}
            ]
        }
    response = client.put(
        "/vacancies/"+str(id_test),
        json=json_vacancy
    )

    assert response.status_code == 422

def test_update_vacancy_fail_user_not_found():
    id_test = uuid.uuid4()
    json_vacancy = {
            "position_name": "Python Senior Dev",
            "company_name": "Test Company",
            "salary": 9999999,
            "currency": "COP",
            "vacancy_link": "https://www.test.com",
            "required_skills":[
                {"Python" : 3},
                {"NoSQL" : 2}
            ]
        }
    response = client.put(
        "/vacancies/"+str(id_test),
        json=json_vacancy
    )

    assert response.json()['status_code'] == 404
    assert response.json()['detail'] == 'Vacancy not found'

"""
    Companies Test
"""
def test_get_all_companies():
    companiesList = []
    if vacanciesList:
        for vacancy in vacanciesList:
            if vacancy.company_name not in companiesList:
                companiesList.append(vacancy.company_name)

    response = client.get("/companies")

    assert response.status_code == 200
    assert response.json() == companiesList

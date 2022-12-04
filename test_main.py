import json 
import uuid

from fastapi.testclient import TestClient
from user import UserRequestModel, UserResponseModel, User, userList

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
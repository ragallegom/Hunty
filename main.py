from fastapi import FastAPI, HTTPException
from user import UserRequestModel, UserResponseModel

users = []

app = FastAPI(
    title='Hunty',
    description='Prueba Tecnica',
    version='1.0.1'
)


@app.get('/')
async def index():
    return {"message": "Hello World"}

@app.post('/users')
async def create_user(user_request: UserRequestModel):
    user = UserRequestModel(
        user_id=user_request.user_id,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        email=user_request.email,
        years_previous_experience=user_request.years_previous_experience,
        skills=user_request.skills
    )

    users.append(user)

    return user

@app.get('/users/{user_id}')
async def get_user(user_id):

    user = next((user for user in users if user.user_id == user_id), None)
    if user:
        return UserResponseModel(
            user_id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            years_previous_experience=user.years_previous_experience,
            skills=user.skills
        )
    else:
        return HTTPException(404, 'User not found')

@app.delete('/users/{user_id}')
async def get_user(user_id):

    user = next((user for user in users if user.user_id == user_id), None)
    
    if user:
        users.remove(user)
        return True
    else:
        return HTTPException(404, 'User not found')
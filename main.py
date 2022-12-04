import uuid
from fastapi import FastAPI, HTTPException
from user import UserRequestModel, UserResponseModel, User, userList

users = userList

app = FastAPI(
    title='Hunty',
    description='Prueba Tecnica',
    version='1.0.1'
)


@app.get('/')
async def index():
    return {"message": "Prueba técnica Hunty"}

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

    user = next((user for user in users if user.user_id == user_id), None)
    if user:
        return User(
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
async def remove_user(user_id):

    user = next((user for user in users if user.user_id == user_id), None)
    
    if user:
        users.remove(user)
        return True
    else:
        return HTTPException(404, 'User not found')

@app.put('/users/{user_id}')
async def update_user(user_id, user_request: UserRequestModel):         
    old_user = next((user for user in users if user.user_id == user_id), None)
    
    if old_user:
        if user_request:
            update_user = User(
                user_id=user_request.user_id,
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
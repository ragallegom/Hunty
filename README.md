# Hunty

Build the image
$ docker build -t fastapi_learn .

Launch the container
$ docker run -d -p 8000:80 fastapi_learn

http://127.0.0.1:8000/

apis
No hay necesidad de usar postman, se deja habilitada la url docs# para las pruebas... desde allí queda se realiza la creación de cada api en openapi
http://localhost:8000/docs#/

test
pytest
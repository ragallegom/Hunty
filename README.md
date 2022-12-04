# Hunty

// construir la imagen  
$ docker build -t fastapi_hunty .

// lanzar el contenedor
$ docker run -d -p 8000:80 fastapi_hunty

// El dockerfile está configurado para localhost 
http://127.0.0.1:8000/

// Apis
No hay necesidad de usar postman, se deja habilitada la url docs# para las pruebas... desde allí queda se realiza la creación de cada api en openapi
http://localhost:8000/docs#/

// Test
pytest
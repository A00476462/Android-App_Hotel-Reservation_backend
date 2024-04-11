Introducation:
This program, built using Django, implements GET POST functionalities for interacting with a MySQL database. Users can perform operations to manage data stored in the connected database.

## The folder of screenshots saved running results

## Please download Python3, MySQL and Django before running the program.

### download Django: pip install Django

## Please change MySQL configuration in settings.py before running, the database configuration information example is as below

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'hotel',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',  # database host address
            'PORT': '3306',       # database port number
        }
    }

## Please run the project by using the command in terminal: python .\manage.py runserver

## "GET" all information from the database in browser example:

### Request:

HTTP method: GET
URL: http://127.0.0.1:8000/app/hotellist/

### Response:

[
{
"id": 1,
"name": "Hotel1",
"price": "123.44",
"email": "hotel1@gmail.com",
"phone": "7821345678"
},
{
"id": 2,
"name": "Hotel2",
"price": "124.55",
"email": "hotel2@gmail.com",
"phone": "7821234567"
}
]

## "GET" a specific hotel information by hotel_id from the database in browser example:

### Request:

HTTP method: GET
URL: http://127.0.0.1:8000/app/hotellist/1/

### Response:

{
"id": 1,
"name": "Hotel1",
"price": "123.44",
"email": "hotel1@gmail.com",
"phone": "7821345678"
}

## "POST" a specific hotel information in browser:

### Request:

HTTP method: POST
URL: http://127.0.0.1:8000/app/hotellist/

### Input the information in Content and Media Type is "application/json":

    {
        "id": 5,
        "name": "Hotel5",
        "price": "205.58",
        "email": "hotel5@gmail.com",
        "phone": "7821236789"
    }

### Response:

HTTP 201 Created
Allow: OPTIONS, GET, POST
Content-Type: application/json
Vary: Accept

{
"id": 5,
"name": "Hotel5",
"price": "205.58",
"email": "hotel5@gmail.com",
"phone": "7821236789"
}

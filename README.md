# balance2.0_backend
### Project creation
(This part just explain the project creation, it should not be made a second time)

py -m venv env  //Create a virtual environment (not mandatory)
env\scripts\activate    //Activate it

pip install django  //Django Installation
django-admin startproject balance   //Creation of the project

cd balance
py manage.py runserver    //Run a first time the server

pip install django-extensions   //Add some Django's extensions
py manage.py startapp webapp    //Creation of the application

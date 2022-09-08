# Project in Django

Prerequisites:
    Python
    Virtualenv (not mandatory)

### Project creation
This part just explain the project creation, it should not be made only once

**py -m venv env**  //Create a virtual environment (not mandatory)
**env\scripts\activate**    //Activate it

**pip install django**  //Django Installation
**pip install django-extensions**   //Install some Django's extensions
(Add 'django_extensions' in INSTALLED_APPS in settings.py)
**django-admin startproject balance**   //Creation of the project

### Run the server
The *manage.py* file allows to executes some commands
**cd balance**  //Enter in the balance folder
**py manage.py runserver**    //Run a first time the server

### Django project vs application
Django is composed of one project and somes applications
Applications can be seen as features

### Create views
Create a *views.py* in the balance folder to manages the views of the project
You can create there function to render html file (see code)

### Create templates
Create a folder *templates* at the root level (same as manage.py)
Create the html files there

### Settings
Configurate the templates folder in the *setting.py*, put 'templates' in *DIRS* in *TEMPLATES*
To tell django where to find templates (in the templates folder at the root)

### Create other pages
In *urls.py* you can link urls to views

### Application
**py manage.py startapp balanceapp**    //Creation of the application

### Save the application in settings
Put *balanceapp* in INSTALLED_APPS in settings.py
(Or *balanceapp.apps.BalanceappConfig* to have the config of the app if we add some configuration)

### Create urls for the app
Create a *urls.py* in the balanceapp folder
In the previous urls.py, add **path('balance/', include('balanceapp.urls'))** to manage the urls from the app in the project (all url starting by *balance/*)

It's better to name the path, to use them in html file

### Parameters/data between views and html files
In the *render* function, you can add parameters: {'var_name': data, ...}
In the html file, you can get it with *Django template* : {{ var_name }}
We can add python code between {% %}
Example to loop the data if it's a list:
*
{% for elem in var_name %}
{{elem}}
{% endfor %}
*

If dictionnary:
{{elem.keyname}}

To know the last element of the loop:
forloop.last (first ; counter ; ...)

There is also {% empty %}, if there is nothing in the for loop / in the data

*
{% if ... %}
{% endif %}
*

*
{{var_name|length}}
*

You can add parameters in urls.py example from another project:
**path('edit/<int:idToEdit>', views.editing)**
Do not forget to add it in parameter to the view (with the same name, *isToEdit* here)

### Class creation
You can create new py file to create classes

### Debug off
If you set debug to false, you have to add the alloweds hosts (in *ALLOWED_HOSTS* in settings.py)

### Models
You can create your models in models.py (in the app file structure)
The id is automatically created

To apply the model, do **py manage.py makemigrations**
Then **py manage.py migrate**

In a class, you can create another class for meta data and add abstract to prevent the instentiation, for utility class like timestamp (?)

### Database config
Can be made in settings.py in DATABASES

### Administration
To manage administration configuration for the model
It's in the admin.py file of the app
Example : **admin.site.register(User, ...)**
The admin panel can be accessed with /admin in the url

You can create a super use with **py manage.py createsuperuser**
You can configure the password strength in AUTH_PASSWORD_VALIDATORS in settings.py

### Style
Add {% load static %} in the html file and 
**<link rel="stylesheet" href="{% static 'style.css' %}">**

And add **STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)** to settings.py

### Launch in production mode 
Add **--insecure** to have the static file adapted

### JSON
**pip install django-jsonfield** and import jsonfield (Problems since Django 4 ?)

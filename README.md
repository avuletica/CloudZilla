# Introduction
CloudZilla is file storage web application written in python (django).
<img src="https://github.com/Bcoolie/CloudZilla/blob/master/static_files/images/dashboard-sample.png" width="480" height="320">

# Installation
Assuming you use virtualenv, follow these steps to download and run the
CloudZilla application:

    $ git clone https://github.com/Bcoolie/CloudZilla
    $ cd CloudZilla
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver


# Compatibility
* Python 2.7, 3.5
* Django 1.9
* SQLite, PostgreSQL, MySQL

# Notes
* If you wish to use contact/registration features you will need to add settings_sensitive file in source
*	You can find template for settings sensitive in source directory
*	For more information visit (https://docs.djangoproject.com/ja/1.9/topics/email/)
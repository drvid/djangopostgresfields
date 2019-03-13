# djangopostgresfields

This is just a sample project/app to demonstrate shortcomings of Django's built-in form widgets for some of the more complex PostgreSQL field types.

The only example is currently an ArrayField of DateTimeRangeFields.

Tested using Django 2.1.7, Python 3.6.7 and PostgreSQL 9.4.21 on Debian Jessie Linux 8.11 (with pyenv).


## Usage

1. Create local PostgreSQL database using name, owner and password defined in `djangopostgresfields/settings.py`.

2. pip install -r requirements.txt

3. python manage.py migrate

4. python manage.py createsuperuser

5. python manage.py runserver

6. Navigate to `/admin`, log in, and try adding a new  _datetimerangearray_ model object.


You will find the HTML form inputs and widgets provided by Django for these fields are nearly impossible to use.


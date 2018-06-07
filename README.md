Articles
=================


Our stack
---------

Back-end:
    - Python 2.7
    - Django 1.10
    - MySQL 5.7
    - Linux

Fron-end:
    - Jquery
    - Bootstrap 3

Third-party services:
    None


Installation
------------

Follow the instructions for setup the project:

1. Clone the project repository from Git::

    $ git clone https://github.com/venkatpython/DjangoRestArticles.git
    # Make Sure you have the access to this repo

2. Create and active local virtual env with below command.
    virtualenv '<env_name>'
    <env_name>/bin/activate

3. Install all required python packages with the below command.
    pip install -r requirements.txt

3. Create DB in mysql with the name "restdb",
    mysql> create database restdb;

4. Run Django Migrations
    python manage.py migrate

5. Start Server and access the application at localhost:8000
    python manage.py runserver



Issues/Tasks/Limitatoins
------------

- Since, there is no user authentication, we can't restrict the user article voting. Single user can vote multiple
  times to a article.
- Design improvements.
- Integrate Authentication to Django REST.
- Use Text editor for Article context.


# Bonsai Marketplace - The Final Project for CS50 by Harvard

This web application is a marketplace for users to buy and sell Bonsai Trees. 

This is not meant to be a production application, but a "proof of concept". No money can be exchanged through the application, by design.

A User can:
- Create an Account
- Log in
- Update their profile data
- Sell a tree
- Buy a tree
- Review their transactions (bought and sold) on their dashboard.
- View and edit all the trees they currently have for sale (via dashboard)

## Tech used

This application was built using Python 3 and:
- Django
- Pytest
- SQLite3
- HTML + CSS
- Bootstrap4

## Setup locally

To get this up and running locally, first clone/fork this repo and `cd` into the `final_project` folder. 

Set up a virtual environment and install dependancies:
```shell
# Create venv
$ python3 -m venv <name_of_env>

# Install dependancies
$ python3 -m pip install -r requirements.txt
```

In order to run this application you will need a `SECRET_KEY`. For securtity reasons this is not hard coded into the `settings.py` file, and instead will be loaded from a `.env` file. To create this file and generate a new `SECRET_KEY` with one _magic_ command:

```shell
$ python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" > bonsai_market/.env
```

Next you will need to create your database and superuser credentials.

```shell
# Make Migrations
$ python3 manage.py makemigrations

# Migrate them to create db tables
$ python3 manage.py migrate

# Create a superuser account (follow the instructions)
$ python3 manage.py createsuperuser
```

You should now be able to start the app and log in with your superuser credentials. Or you can create a normal user account, too. Run the app with:
```shell
$ python3 manage.py runserver
```

Happy Bonsai-ing (completely made up word)

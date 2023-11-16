Backend Assignment
====


## Getting started

### Prerequisites

* Linux or Mac OSx
* python-dev and libpq-dev packages
* PostgreSQL database server (>=14.9)
* Python 3
* Virtualenv

### Installation

* Create a new virtualenv and activate it.

```
virtualenv venv
source ./venv/bin/active
```
*  Install all the dependencies

```
pip install -r requirements.txt
```
* Create a PostgreSQL Database and update the details in settings.py file
* Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

* Run the server

```
python manage.py runserver 0.0.0.0:8000
```
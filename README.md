# Know Your Body Backend
---

This repository contains backend application for [Know Your Body Frontend](https://github.com/Know-Your-Body/Know-Your-Body-Frontend).

### How To Build

For MacOS/Linux
```sh
git clone git@github.com:Know-Your-Body/Know-Your-Body-Backend.git
cd Know-Your-Body-Backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

### API Docs

1. User Sign Up

```
POST /api/user/signup
```

__Parameters__

Name         | Description
-------------|-------------------------------------
username     | username for the user
password     | password for the user of atleast 8 characters

__Request__
```json
{
    "username": "shashank",
    "password": "mynewpass"
}
```

__Response__
```json

Status: 201 OK
{
    "token": "ceaf8dbebfd783b321ba570894d5f7f1a123bc53",
}
```

2. User Sign In

```
POST /api/user/signin
```

__Parameters__

Name         | Description
-------------|-------------------------------------
username     | username for the user
password     | password for the user of atleast 8 characters

__Request__
```json
{
    "username": "shashank",
    "password": "mynewpass"
}
```

__Response__
```json

Status: 200 OK
{
    "token": "ceaf8dbebfd783b321ba570894d5f7f1a123bc53",
}
```

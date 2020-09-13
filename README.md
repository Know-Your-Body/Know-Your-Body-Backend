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
pip install -r requirements.txt
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

Status: 201 Created
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

3. Saving User's Body Mass Index data

```
POST /api/user/bmi Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Parameters__

Name         | Description
-------------|-------------------------------------
height       | height in decimal
weight       | weight in decimal

__Request__
```json
{
    "height": 172,
    "weight": 85
}
```

__Response__
```json

Status: 201 Created
{
    "id": "9e6678af-b758-4710-a657-73d5ad189518",
    "created_at": "2020-09-13T11:23:02.557053Z",
    "height": "172.00",
    "weight": "85.00",
    "user": 5
}
```

4. Getting User's previous Body Mass Index data

```
GET /api/user/bmi Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Response__
```json

Status: 200 Ok
[
    {
        "id": "3c8ae4b3-62d2-45ff-8e8a-867478f2d8d1",
        "created_at": "2020-09-13T10:47:49.744496Z",
        "height": "70.00",
        "weight": "120.00",
        "user": 5
    },
    {
        "id": "4e329ee4-c9d6-43cf-87b4-c610eb182835",
        "created_at": "2020-09-13T10:53:50.017405Z",
        "height": "70.20",
        "weight": "120.00",
        "user": 5
    },
    {
        "id": "9e6678af-b758-4710-a657-73d5ad189518",
        "created_at": "2020-09-13T11:23:02.557053Z",
        "height": "172.00",
        "weight": "85.00",
        "user": 5
    }
]
```

5. Saving User's Hemoglobin data

```
POST /api/user/hemoglobin Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Parameters__

Name                | Description
--------------------|-------------------------------------
hemoglobin_level    | hemoglobin level in decimal
gender              | "F" for Femal or "M" for Male

__Request__
```json
{
    "hemoglobin_level": 13,
    "gender": "M"
}
```

__Response__
```json

Status: 201 Created
{
    "id": "a125c31e-86f6-494e-ab0a-3c1d3d613a0a",
    "created_at": "2020-09-13T11:26:27.152690Z",
    "hemoglobin_level": "13.00",
    "gender": "M",
    "user": 5
}
```

6. Getting User's previous Hemoglobin data

```
GET /api/user/hemoglobin Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Response__
```json

Status: 200 Ok
[
    {
        "id": "8e567e59-5b18-4724-9ff8-633bb4dabe12",
        "created_at": "2020-09-13T11:00:01.421759Z",
        "hemoglobin_level": "13.00",
        "gender": "M",
        "user": 5
    },
    {
        "id": "a125c31e-86f6-494e-ab0a-3c1d3d613a0a",
        "created_at": "2020-09-13T11:26:27.152690Z",
        "hemoglobin_level": "13.00",
        "gender": "F",
        "user": 5
    }
]
```

7. Saving User's Bloog Sugar data

```
POST /api/user/bloodsugar Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Parameters__

Name                | Description
--------------------|-------------------------------------
blood_sugar_level   | Blood Sugar level in decimal at fasting

__Request__
```json
{
    "blood_sugar_level": 94
}
```

__Response__
```json

Status: 201 Created
{
    "id": "07afecbe-04cb-403f-8bc4-6757c762cbac",
    "created_at": "2020-09-13T11:04:53.276198Z",
    "blood_sugar_level": "94.00",
    "user": 5
}
```

8. Getting User's previous Blood Sugar data

```
GET /api/user/bloodsugar Authorization: Token ceaf8dbebfd783b321ba570894d5f7f1a123bc53
```

__Response__
```json

Status: 200 Ok
[
    {
        "id": "07afecbe-04cb-403f-8bc4-6757c762cbac",
        "created_at": "2020-09-13T11:04:53.276198Z",
        "blood_sugar_level": "94.00",
        "user": 5
    }
]
```

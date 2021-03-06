# Keeper Solutions
Keeper Solutions is an international software services firm with global reach with head office located in Limerick, Ireland, and delivery centers in Croatia, Serbia, Romania, and Costa Rica. We are growing our team and we are looking for people who possess a positive attitude and who enjoy working in a relaxed professional environment alongside some very smart and motivated people.

## TASK ASSIGNEMENT: Web Bookmarks

Create a REST api for web bookmarks. These bookmarks can be private or public. After authentication, users can create and delete / update their bookmarks. They can also view their bookmarks and other users public bookmarks. Anonymous users can only view public bookmarks.
Every bookmark should have "title","url" and "created_at" fields. Other fields are up to you. 
Additional important notes:
- create a public repo on Github containing the code (we are using Github for our project)
- use latest versions of Django / Django Rest Framework; no other package is required for this task (DRF BasicAuthentication can be used)
- write tests (the bigger coverage, the better)
- please provide a script for running the endpoints (a text file with list of curl commands should do)
- add a readme file of project setup / test running

## Installation

Install the dependencies and start the server.

- python 3.8
- pip

Create a virtualenv

```sh
git clone https://github.com/emartinez1015/keepersoltest.git
cd keepersoltest
pip install -r requeriments.txt
python manage.py runserver 8000
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## REST API
#### Login
```
curl --location --request POST 'http://127.0.0.1:8000/api/user/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "edgar@gmail.com",
    "password": "sebasysofi25"
}'
```
#### Response Login
```
{
    "user": {
        "username": "edgar@gmail.com",
        "first_name": "",
        "last_name": "",
        "email": "edgar@gmail.com"
    },
    "access_token": "73ddb3714eee6ecdda900a95b7199034557e814a"
}
```

## For the next endpoints

#### Get BookMarks

```
curl --location --request GET 'http://127.0.0.1:8000/api/bookmark' \
--header 'Authorization: Token 73ddb3714eee6ecdda900a95b7199034557e814a'
```

#### Create BookMarks
```
curl -X POST \
  http://localhost:8000/api/bookmark \
  -H 'authorization: Token 73ddb3714eee6ecdda900a95b7199034557e814a' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"title": "Test 3",
	"url": "test3.com",
	"owner":1
}'
```

### Update BookMarks
```
curl -X PUT \
  http://localhost:8000/api/bookmark \
  -H 'authorization: Token 73ddb3714eee6ecdda900a95b7199034557e814a' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"id": 2,
	"title": "Test 3",
	"url": "test3.com",
	"owner":1
}'
```

### Delete BookMarks
```
curl -X DELETE \
  http://localhost:8000/api/bookmark/2 \
  -H 'authorization: Token 73ddb3714eee6ecdda900a95b7199034557e814a' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' 
```


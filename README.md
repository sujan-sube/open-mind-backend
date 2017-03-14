# OpenMind Backend API

## API Endpoints
### 1. Google Login
#### Endpoint: `/rest-auth/google/`
Methods: `[Post]`

Request Header: `None`

Request Body: 
```javascript
{ 
    "access_token": "",
    "code": "{serverAuthCode}"
}
```

Response:
```javascript
{ 
    "key": "{token}"
}
```
### 2. Local Registration
#### Endpoint: `/rest-auth/registration/`
Methods: `[Post]`

Request Header: `None`

Request Body: 
```javascript
{ 
    "username": "{username}",
    "password1": "{password}",
    "password2": "{password}"
}
```
Response:
```javascript
{ 
    "key": "{token}"
}
```
### 3. Local Login
#### Endpoint: `/rest-auth/login/`
Methods: `[Post]`

Request Header: `None`

Request Body: 
```javascript
{ 
    "username": "{username}",
    "password": "{password}"
}
```
Response:
```javascript
{ 
    "key": "{token}"
}
```
### 4. User Profile
#### Endpoint: `/rest-auth/user/`
**! Requires Authenticated User**
Methods: `[Get]`

Request Header:
```
Authorization: Token {Token}
```
Request Body: `None`

Response:
```javascript
{ 
    "pk": {primary key},
    "username": "{username}",
    "email": "{email}",
    "first_name": "{first name}",
    "last_name": "{last name}"
}
```
### 4. Journal
#### Endpoint: `/journal/`
**! Requires Authenticated User**

Methods: `[Get, Post]`

Request Header `[Get, Post]`:
```javascript
Authorization: Token {Token}
```
Request Body `[Get]`: `None`

Request Response `[Get]`:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of journal entries}
    ]
}
```
Request Body `[Post]`:
```javascript
{ 
    "date": {date},
    "content": {content}
}
```
Response `[Post]`:
```javascript
{
    "user": "{user primary key}",
    "date": "{date}",
    "content": "{content}",
    "analysis": {sentiment analysis result},
    "analysis_comment": "{sentiment analysis comment}"
}
```
#### Endpoint: `/journal/?date={date}`
**! Requires Authenticated User**

**{date} format: YYYY-MM-DD**

Methods: `[Get]`

Request Header:
```javascript
Authorization: Token {Token}
```
Request Body: `None`

Request Response:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of journal entries}
    ]
}
```
#### Endpoint: `/journal/?daterange_0={date}&daterange_1={date}`
**! Requires Authenticated User**

**{date} format: YYYY-MM-DD**

Methods: `[Get]`

Request Header:
```javascript
Authorization: Token {Token}
```
Request Body: `None`

Request Response:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of journal entries}
    ]
}
```

## Django Fixtures
Django fixtures saves the contents of a database into a json file. The json file can then be loaded to restore the data to the database.

### Create Fixtures
Run the following command to dump the data of a specific app to a json file.
- `python manage.py dumpdata --format=json myapp > /path/to/myapp/fixtures/myapp_test.json`

### Load Fixtures
Run the following command to load the data from a json file. Django will search the entire project for a json matching the provided argument.
- `python manage.py loaddata myapp_test`

### Clear Database
To clear the data for a specific app use the following commands:

1. `python manage.py migrate myapp zero`
2. `python manage.py migrate`

To clear the data from the entire database (all apps) use the following command:
- `python manage.py flush`

## Generating Test Data
The command to create test data is in the format:
- `python manage.py loadtestdata app.Model:#`

To generate test data for the Emotion and Journal models run the following command:
- `python manage.py loadtestdata emotion.Emotion:10 journal.Journal:10`
# OpenMind Backend API

## API Endpoints
### 1. Google Login
#### Endpoint: `/rest-auth/google/`
Methods: `[Post]`
Request Header: `None`
Request Body: 
```json
{ 
    access_token = "",
    code = "{serverAuthCode}"
}
```
Response:
```json
{ 
    key = "{token}"
}
```
### 2. Local Registration
#### Endpoint: `/rest-auth/registration/`
Methods: `[Post]`
Request Header: `None`
Request Body: 
```json
{ 
    username = "{username}",
    password1 = "{password}",
    password2 = "{password}"
}
```
Response:
```json
{ 
    key = "{token}"
}
```
### 3. Local Login
#### Endpoint: `/rest-auth/login/`
Methods: `[Post]`
Request Header: `None`
Request Body: 
```json
{ 
    username = "{username}",
    password = "{password}"
}
```
Response:
```json
{ 
    key = "{token}"
}
```
### 4. User Profile
#### Endpoint: `/rest-auth/user/`
**! Requires Authenticated User**
Methods: `[Get]`
Request Header:
```json
Authorization: Token {Token}
```
Request Body: `None`
Response:
```json
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
```json
Authorization: Token {Token}
```
Request Body `[Get]`: `None`
Request Response `[Get]`:
```json
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
```json
{ 
    date = {date},
    content = {content}
}
```
Response `[Post]`:
```json
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
```json
Authorization: Token {Token}
```
Request Body: `None`
Request Response:
```json
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of journal entries}
    ]
}
```

## Generating Test Data
The command to create test data is in the format:
- `python manage.py loadtestdata app.Model:#`

To generate test data for the Emotion and Journal models run the following command:
- `python manage.py loadtestdata emotion.Emotion:10 journal.Journal:10`

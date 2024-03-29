# OpenMind Backend API

## API Endpoints
### 1. Google Login
#### Endpoint: `/rest-auth/google/`
Methods: `[Post]`

Request Header: `None`

Request Body: 
```javascript
{ 
    "token": {id token from Google},
}
```

Response:
```
200
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
token: {id token from google}
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
### 5. Journal
#### Endpoint: `/journal/`
**! Requires Authenticated User**

Methods: `[Get, Post]`

Request Header `[Get, Post]`:
```javascript
token: {id token from google}
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
token: {id token from google}
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
token: {id token from google}
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
### 6. Emotion
#### Endpoint: `/emotion/`
**! Requires Authenticated User**

Methods: `[Get, Post]`

Request Header `[Get, Post]`:
```javascript
token: {id token from google}
```
Request Body `[Get]`: `None`

Request Response `[Get]`:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of emotion entries}
    ]
}
```
Request Body `[Post]`:
```javascript
Type: form-data
    date = {date}
    image = {image file}
```
Response `[Post]`:
```javascript
{
    "user": "{user primary key}",
    "date": "{date}",
    "image": "{image url}",
    "max_expression": "{expression with the max score value}",
    "expressions": {dictionary of expression-score values}
}
```
#### Endpoint: `/emotion/?date={date}`
**! Requires Authenticated User**

**{date} format: YYYY-MM-DD**

Methods: `[Get]`

Request Header:
```javascript
token: {id token from google}
```
Request Body: `None`

Request Response:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of emotion entries}
    ]
}
```
#### Endpoint: `/emotion/?daterange_0={date}&daterange_1={date}`
**! Requires Authenticated User**

**{date} format: YYYY-MM-DD**

Methods: `[Get]`

Request Header:
```javascript
token: {id token from google}
```
Request Body: `None`

Request Response:
```javascript
{
    "count": {number of items},
    "next": "{url to next page}",
    "previous": "{url to next page}",
    "results": [
        {array of emotion entries}
    ]
}
```
## Django Fixtures
Django fixtures saves the contents of a database into a json file. The json file can then be loaded to restore the data to the database.

### Create Fixtures
Run the following command to dump the data of a specific app to a json file.
- `python manage.py dumpdata --format json --indent 4 myapp > /path/to/myapp/fixtures/myapp_test.json`

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

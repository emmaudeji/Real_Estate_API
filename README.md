# Property Management API

API designed to serve property management application. It performs CRUD functionalities for 3 user model, and Property data. The user model includes public user, registered user, Agents. The database is designed with Postgres and uses the flask-migrate package to update the database. 

## Quick Set-up

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - It's commendable to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
  pip install -r requirements.txt
```
### Alternative set-up
To get started quickly, follow this steps
- install python-pipenv: `pip install pipenv` [learn more about pipenv](https://pipenv.pypa.io/en/latest/install/).
- install dependencies from the Pipfile using `pipenv install` 
- activate the the virtual environment using `pipenv shell` 
- set up the database. Check below.
- run flask app from the .flaskenv using `flask run` 
- Test with curl `http://127.0.0.1:5000/properties` 

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `housify` database:

```bash
createbd housify
```

Populate the database using the `housify.psql` file provided. From the root directory in terminal run:

```bash
psql housify < housify.psql
```

### Run the Server

From within the `root` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## API Reference

### General

- Base URL: this app is hosted locally under the port 5000. The API base URL is `http://localhost:5000/`
- Authentication: this app doesn't require any authentication or API tokens.
- You must set the header: `Content-Type: application/json` with every request.

### Error Handlers

if any errors accured, the API will return a json object in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The following errors will be reported:

- 400: `bad request`
- 404: `resource not found`
- 405: `method not allowed`
- 422: `unprocessible`

### Endpoints

#### GET `/users`

- Fetches a array of users details.
- Request Arguments: None
- Returns: An array object that contains list of user objects which is a dictionary containing the details of each user in the list.
- example: `curl http://localhost:5000/users -H "Content-Type: application/json"`

```
{
  "success": true,
  "users": [
    {
      "created_at": "Tue, 01 Nov 2022 17:39:00 GMT",
      "email": "x@x.com",
      "id": 14,
      "isAgent": true,
      "username": "x"
    },
    {
      "created_at": "Tue, 18 Oct 2022 16:21:15 GMT",
      "email": "z@z.com",
      "id": 13,
      "isAgent": true,
      "username": "z"
    },
    {
      "created_at": "Sun, 06 Nov 2022 20:54:56 GMT",
      "email": "m@m.com",
      "id": 15,
      "isAgent": true,
      "username": "Mildred"
    },
    {
      "created_at": "Mon, 07 Nov 2022 11:18:50 GMT",
      "email": "s@s.com",
      "id": 16,
      "isAgent": true,
      "username": "Sophia"
    },
    {
      "created_at": "Mon, 07 Nov 2022 12:09:04 GMT",
      "email": "b@b.com",
      "id": 17,
      "isAgent": true,
      "username": "Bonny Luke"
    },
    {
      "created_at": "Mon, 14 Nov 2022 06:59:15 GMT",
      "email": "zelipha@gmail.com",
      "id": 18,
      "isAgent": false,
      "username": "zelipha"
    },
    {
      "created_at": "Mon, 14 Nov 2022 07:35:53 GMT",
      "email": "c@c.com",
      "id": 19,
      "isAgent": true,
      "username": "Cynthia"
    },
    {
      "created_at": "Fri, 25 Nov 2022 12:24:13 GMT",
      "email": "w@w.com",
      "id": 20,
      "isAgent": true,
      "username": "Winner"
    }
  ]
}
```

#### GET `/agents`

- Fetches an object of the list of agent objects.

```
{
    [
     {
      "address": "7 Mcc Road, Opposite Edmark, Owerri.",
      "bio": "Expert realtor with 21 years experience in property developemnt and management",
      "country": "Nigeria",
      "created_at": "Mon, 07 Nov 2022 12:10:51 GMT",
      "email": "bonny@gmail.com",
      "fullname": "Bonny Lukes",
      "id": 9,
      "linkedin": "www.linkedin.com/in/bonnyL",
      "phonenumber": 333333,
      "profilePic": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAO3UY3ptiW9qfp5du+MK/KFRyhtDaQobjZAAJPTPvWfFcN7RAQOY1CH4ZNwpRe6WnHF8uVbY/01padWtKg6PLnB3Fe/eMJU2tBSpJIVzZyCOua0FxaVKIbPKevrXiPivWr//Z",
      "twitter": "@bonny",
      "user_id": 17
    },
    {
      "address": "12 Luca Avenue, Street 5",
      "bio": "Professional realtor with ability to discover potential markets and make maximum returns for the client.",
      "country": "Uzoket, Brazil",
      "created_at": "Mon, 14 Nov 2022 06:50:21 GMT",
      "email": "sophianoles@gmail.com",
      "fullname": "Sophia Noles",
      "id": 8,
      "linkedin": "www.linkedin.com/in/sophia-noles",
      "phonenumber": 3333334,
      "profilePic": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4gxYSUNDX1BST0ZJTEUAAQEAAAxITGlubwIQAABtbnRyUkdCIFhZWiAHzgACAAkABgAxAABhY3NwTVNGVAAAAABJRUMgc1JHQgAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLUhQICAAA7nJJ9DOMe85UfeaSxWoZSckCIoepnI6nze/vPEq/P/yVW/eBmH2lZUrAfJCTB2gPE+uWeaw59BPoiDLTQkh7B6pMAVsvYgj/ALnivF7Y7EKPsBLBjp3gJxP/2Q==",
      "twitter": "@sophiaNoles",
      "user_id": 16
    },
  ],
  "success": true
 }

```

```
#### GET `/properties`
Fetches object containing list all property objects created by an agent

  Example Property object.
    
  {
    "feedback": [
        {
            "address": "1015 Florida Street",
            "agent_id": 9,
            "bedroom": null,
            "country": "Nairobi, Kenya",
            "created_at": "Mon, 07 Nov 2022 12:14:17 GMT",
            "description": "Can only pick drinks and view drink details",
            "id": 33,
            "price": 2222,
            "property_type": "Bungalow",
            "user_id=": null,
            "view1": null,
            "view2": null,
            "view3": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4QAqRXhpZgAASUkqAANtdUxUGq2LoyYsWouLHuAPEdg4AjuO7gQNMMAMkWVip3g2Nu7AAKKYg3BItxGh9WGKhfTPnNtzHcRopsCdRwOm8aHs44qxUcD4oAxDgoBTHV8CLjh2jwPDw1HdhUIUPT6Bhua9r79N9xu9d9ewYQARikJhijFkUf/2Q==",
            "view4": "data:image/jpeg;base64,/9j/4AAQSk5e2CZMctv2TTq3f213baGXssh2h3eW2ezLzYBxcLXNC1IpZkIG3GLYDy3wIANPBVrODZcqRQkWEZBtDOcnTGRoukDYtRda6CDrJI0wANU2LyVncSFJd9KGCzgmQQegCNsjFbfEs7PGUN9tYhY73EBLvPGZm6lsNtL5Cs02RPqsFyrABMA9yUCttSS8ONrpVucRAaru3keZtEObZxEq6mNjLurs+xFQTQvAG+mJeq1v7GPTM+xAKJ/9k="
        },
     {
      ...
     },
    ],
    "success": true
}


```

```
GET Wisglist
/wishlist/<user_id>/properties

  {
    "feedback": [
        {
            "address": "1015 Florida Street",
            "agent_id": 9,
            "bedroom": null,
            "country": "Nairobi, Kenya",
            "created_at": "Wed, 09 Nov 2022 13:14:34 GMT",
            "description": "Can only pick drinks and view drink details",
            "id": 18,
            "price": 2222,
            "property_id": 33,
            "property_type": "Bungalow",
            "user_id=": 14,
            "view1": null,
            "view2": null,
            "view3": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4QAqRXhpZgAASUkqriCN48DwOLTMmLqZ81+DAFj2ECwO70W13AWP4NtdUxUGq2LoyYsWouLHuAPEdg4AjuO7gQNMMAMkWVip3g2Nu7AAKKYg3BItxGh9WGKhfTPnNtzHcRopsCdRwOm8aHs44qxUcD4oAxDgoBTHV8CLjh2jwPDw1HdhUIUPT6Bhua9r79N9xu9d9ewYQARikJhijFkUf/2Q==",
            "view4": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEBLAEsAAD/2wBJX/ACFE12CkwQ5Z9JNpcAVlYSXlNq5cGtSzQmYAcQGdGonLZLO2gZ9lIkI1Z9EAunF+sQaPX4iUuWNfpNREuzFXXmxBSkaicRAaru3keZtEObZxEq6mNjLurs+xFQTQvAG+mJeq1v7GPTM+xAKJ/9k="
        },



```


## Testing

The app uses `unittest` for testing all functionalities. Create a testing database and store the URI in the `TEST_DATABASE_URI` environment.
To run the tests, run

```
bash
# if exists, drop the testing database and create it again
dropdb trivia_test
createdb trivia_test
# restore the trivia dump file to the testing database
psql trivia_test < trivia.psql
# finally, from the `backend` directory, run
python test_flaskr.py
```

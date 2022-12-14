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
#### GET `/agents`




```
#### GET `/categories/<int:id>/questions`

- Fetches a dictionary of paginated questions that are in the category specified in the URL parameters.
- Request Arguments:
  - optional URL queries:
    - `page`: an optional integer for a page number, which is used to fetch 10 questions for the corresponding page.
    - default: `1`
- Returns: An object with 3 keys:
  - str:`current_category`: a string that contains the category type for the selected category.
  - `questions`: a list that contains paginated questions objects, that coorespond to the `page` query.
    - int:`id`: Question id.
    - str:`question`: Question text.
    - int:`difficulty`: Question difficulty.
    - int:`category`: question category id.
  - int:`total_questions`: an integer that contains total questions in the selected category.
- example: `curl http://localhost:5000/api/v1/categories/1/questions -H "Content-Type: application/json"`

```
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 3,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Me, duh!",
      "category": 1,
      "difficulty": 5,
      "id": 24,
      "question": "Who invented electricity?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

#### DELETE `/questions/<int:id>`

- Deletes the question by the id specified in the URL parameters.
- Request Arguments: None
- Returns: A dictionary that contain deleted: question_id key:value pair.
- example: `curl -X DELETE http://localhost:5000/api/v1/questions/20 -H "Content-Type: application/json"`

```
{
    "deleted": 2,
    "success": true
}
```

#### POST `/questions/search`

- search for a question.
- Request Arguments:
  - Json object:
    - str:`searchTerm`: a string that contains the search term to search with.
- returns: an object with the following:
  - `questions`: a list that contains paginated questions objects, durrived from the search term.
    - int:`id`: Question id.
    - str:`question`: Question text.
    - int:`difficulty`: Question difficulty.
    - int:`category`: question category id.
  - int:`total_questions`: an integer that contains total questions returned from the search.
- example: `curl -X POST http://localhost:5000/api/v1/questions -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`

```
{
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 3,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 2,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

#### POST `/questions`

- posts a new question.
- Request Arguments:
  - Json object:
    - str:`question`: A string that contains the question text.
    - str:`answer`: A string that contains the answer text.
    - int:`difficulty`: An integer that contains the difficulty, please note that `difficulty` can be from 1 to 5.
    - int:`category: An integer that contains the category id.
- Returns: an object with the following keys:
  - int:`id`: an integer that contains the ID for the created question.
  - str:`question`: A string that contains the text for the created question.
  - `questions`: a list that contains paginated questions objects.
    - int:`id`: Question id.
    - str:`question`: Question text.
    - int:`difficulty`: Question difficulty.
    - int:`category`: question category id.
  - int:`total_questions`: an integer that contains total questions.
- example: `curl -X POST http://localhost:5000/api/v1/questions -H "Content-Type: application/json" -d '{ "question": "What is the application used to build great python backends?", "answer": "Flask", "difficulty": 2, "category": 1}'`

```
{
    "id": 34,
    "question": "What is the application used to build great python backends?",
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        }
    ],
    "success": true,
    "total_questions": 27
}
```

#### POST `/quizzes`

- allows the user to play the quiz game, returning a random question that is not in the previous_questions list.
- Request Arguments:
  - Json object:
    - `previous_questions`: A list that contains the IDs of the previous questions. If starting the game for the first time, you can post an empty list.
    - `quiz_category`: A dictionary that contains the category id and category type.
      - int:`id`: the category id to get the random question from.  
        use `0` to get a random question from all categories.
      - str:`type`: an optional value for the category type.  
        Please note that this variable is provided only for convenience, and it will not have any effect on getting the question.
- returns: a question dictionary that has the following data: - int:`id`: An integer that contains the question ID. - str:`question`: A string that contains the question text. - str:`answer`: A string that contains the answer text. - int:`difficulty`: An integer that contains the difficulty. - int:`category: An integer that contains the category ID.
- Examples:
  - request a random question with previous questions and the category "science":  
    `curl -X POST http://localhost:5000/api/v1/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [21], "quiz_category": {"type": "Science", "id": 1}}'`
  - request with no previous questions, for a random question from all categories:  
     `curl -X POST http://localhost:5000/api/v1/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id": 0}}'`
    Sample return:

```
{
    "question": {
        "answer": "Flask",
        "category": 1,
        "difficulty": 2,
        "id": 42,
        "question": "What is the application used to build great python backends?"
    },
    "success": true
}
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

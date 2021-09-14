# Full Stack Web Developer Nanodegree - Capstone

## Motivation & Background

This is the final project of the Udactiy Full Stack Web Developer Nanodegree. 
The project It is a Flask app that is used to manage a casting agency.

There are two database models

- Movie with attributes title and release date
- Actor with attributes name, age and gender

and three roles 

- Casting Assistant with permission to view movies and actors
- Casting Director with permissions of Casting Assistant plus the permission to add or delete actors from the database and the permission to modify actors and movies
- Executive Producer with the permissions of Casting Director plus the permission to add or delete movies to the database

The roles are managed in Auth0 and the permissions are added to the access token.

## Getting Started

### Installing Dependencies

Install necessary dependencies with  
```bash
pip install -r requirements.txt
```

### Setting up the Database
With Postgres running, run
```bash
dropdb capstone
createdb capstone
psql capstone < capstone.psql
```

### Running the local server
Run the application locally with  
```bash
export FLASK_APP=app.py
export FLASK_ENVIRONMENT=development
flask run --reload
```
Use a virtual environment if you wish to with  
```bash
python3 venv venv
source venv/bin/activate
```

## Running the Application
If you are running the app locally navigate to http://localhost:5000/    
If you want to use the live app navigate to https://fsdn-capstone-app-310821.herokuapp.com/  

## Running the Tests
To run the tests, run
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone.psql
python test_app.py
```

## API Reference

### Endpoints

GET '/movies'

- returns the list of movies saved on the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/movies
- sample response 
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 31 Aug 2001 23:00:00 GMT",
            "title": "Harry Potter and the Philosopher's Stone"
        },
        {
            "id": 17,
            "release_date": "Sat, 31 Aug 2002 23:00:00 GMT",
            "title": "Harry Potter and the Chamber of Secrets"
        }
    ],
    "success": true
}
```

GET '/actors'
- returns the list of actors saved on the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/actors
- sample response
```
{
    "actors": [
        {
            "id": 1,
            "name": "Alan Rickman",
            "age": 69,
            "gender": "male"
        },
        {
            "id": 2,
            "name": "Maggie Smith",
            "age": 86,
            "gender": "female"
        }
    ],
    "success": true
}
```

POST '/movies'
- add a movie to the list of movies saved on the database
- sample request https://fsdn-capstone-app-310821.herokuapp.com/movies
with body  
```
{
    "title": "Harry Potter and the Philosopher's Stone",
    "release_date": "31/07/2001"
}
```
- sample response
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 31 Aug 2001 23:00:00 GMT",
            "title": "Harry Potter and the Philosopher's Stone"
        },
        {
            "id": 2,
            "release_date": "Sat, 31 Aug 2002 23:00:00 GMT",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "id": 3,
            "release_date": "Tue, 31 Aug 2004 23:00:00 GMT",
            "title": "Harry Potter and the Prisoner of Azkaban"
        }
    ],
    "success": true
}
```

POST '/actors'
- add an actor or actess to the list of movies saved on the database
- sample request https://fsdn-capstone-app-310821.herokuapp.com/actors
with body  
```
{
    "name": "Emma Watson",
    "age": 31,
    "gender": "female
}
```
- sample response
```
{
    "actors": [
        {
            "id": 1,
            "name": "Alan Rickman",
            "age": 69,
            "gender": "male"
        },
        {
            "id": 2,
            "name": "Maggie Smith",
            "age": 86,
            "gender": "female"
        },
        { 
            "id": 3,
            "name": "Emma Watson",
            "age": 31,
            "gender": "female"

        }
    ],
    "success": true
}
```

PATCH 'movies/{id}'
- update a movie on the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/movies/1
with body  
```
{
    "title": "Harry Potter and the Philosopher's Stone",
    "release_date": "31/07/2001"
}
```
- sample response
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 31 Aug 2001 23:00:00 GMT",
            "title": "Harry Potter and the Philosopher's Stone"
        },
        {
            "id": 2,
            "release_date": "Sat, 31 Aug 2002 23:00:00 GMT",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "id": 3,
            "release_date": "Tue, 31 Aug 2004 23:00:00 GMT",
            "title": "Harry Potter and the Prisoner of Azkaban"
        }
    ],
    "success": true
}
```

PATCH 'actors/{id}'
- update an actor or actress on the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/actors/1
with body  
```
{
    "name": "Alan Rickman"
}
```
- sample response
```
{
    "actors": [
        {
            "id": 1,
            "name": "Alan Rickman",
            "age": 69,
            "gender": "male"
        },
        {
            "id": 2,
            "name": "Maggie Smith",
            "age": 86,
            "gender": "female"
        },
        { 
            "id": 3,
            "name": "Emma Watson",
            "age": 31,
            "gender": "female"

        }
    ],
    "success": true
}
```

DELETE 'movies/{id}'
- delete a movie from the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/movies/1
- sample response
```
{
    "movie_id": 1,
    "success": true
}
```

DELETE 'actors/{id}'
- delete an actor or actress from the server
- sample request https://fsdn-capstone-app-310821.herokuapp.com/actors/1
- sample response
```
{
    "actor_id": 1,
    "success": true
}
```

### Error Handling

401 Unauthorized

404 Resource not found

405 Method not allowed

422 Unprocessable

Sample Response for an error
```
{
    "error": 404,
    "message": "resource not found",
    "success": false
}
```


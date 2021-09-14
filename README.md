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

## Getting Started

## Running the Application

## Running the Tests

## API Reference

### Endpoints

GET '/movies'

- returns the list of movies saved on the server
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
- neccessary attributes are title and release date
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
- neccessary attributes are name, age and gender
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
- neccessary attributes at least one of the attributes of a movie
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
- necessary attributes at least on of the attributes of an actor or an actress
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
- sample response
```
{
    "movie_id": 1,
    "success": true
}
```

DELETE 'actors/{id}'
- delete an actor or actress from the server
- sample response
```
{
    "actor_id": 1,
    "success": true
}
```

### Error Handling

401

404

405

422


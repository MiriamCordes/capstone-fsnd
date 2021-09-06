import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  return app


APP = create_app()

@APP.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization,true'
        )
    response.headers.add(
      'Access-Control-Allow-Methods',
      'GET,PUT,POST,DELETE,PATCH'
    )
    return response

# Routing for movies

@APP.route('/movies', methods=["GET"])
@requires_auth('get:movies')
def get_movies():
  try:
    movies = Movie.query.all()

    if movies is None: 
      abort(422)

    formatted_movies = [movie.format() for movie in movies]

    return jsonify({
      "movies": formatted_movies,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


@APP.route('/movies/<int:movie_id>', methods=["DELETE"])
@requires_auth('delete:movie')
def delete_movie(movie_id):
  movie = Movie.query.get(movie_id)

  if movie is None:
    abort(404)

  try:
    movie.delete()

    return jsonify({
      "movie_id": movie.id,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


@APP.route('/movies', methods=["POST"])
@requires_auth('create:movie')
def create_movie():
  body = request.get_json()

  if body is None:
    abort(422)

  movie_title = body.get('title', None)
  movie_release_date = body.get('release_date', None)

  if movie_title is None or movie_release_date is None: 
    abort(422)

  try: 
    movie = Movie(title=movie_title, release_date=movie_release_date)
    movie.insert()

    movies = Movie.query.all()
    formatted_movies = [movie.format for movie in movies]

    return jsonify({
      "movies": formatted_movies,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)

@APP.route('/movies/<int:movie_id>', methods=["PATCH"])
@requires_auth('update:movie')
def update_movie(movie_id):
  movie = Movie.query.get(movie_id)

  if movie is None: 
    abort(404)

  body = request.get_json()

  if body is None:
    abort(422)

  movie_title = body.get('title', None)
  movie_release_date = body.get('release_date', None)

  if movie_title is not None:
    movie.title = movie_title

  if movie_release_date is not None:
    movie.release_date = movie_release_date

  try: 
    movie.update()

    movies = Movie.query.all()
    formatted_movies = [movie.format for movie in movies]

    return jsonify({
      'movies': formatted_movies,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


#Routing for actors
@APP.route('/actors', methods=["GET"])
@requires_auth('get:actors')
def get_actors():
  try:
    actors = Actor.query.all()

    if actor is None: 
      abort(422)

    formatted_actors = [actor.format() for actor in actors]

    return jsonify({
      "actors": formatted_actors,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


@APP.route('/actors/<int:actor_id>', methods=["DELETE"])
@requires_auth('delete:actor')
def delete_actor(actor_id):
  actor = Actor.query.get(actor_id)

  if actor is None:
    abort(404)

  try:
    actor.delete()

    return jsonify({
      "actor_id": actor.id,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


@APP.route('/actors', methods=["POST"])
@requires_auth('create:actor')
def create_actor():
  body = request.get_json()

  if body is None:
    abort(422)

  actor_name = body.get('name', None)
  actor_age = body.get('age', None)
  actor_gender = body.get('gender', None)

  if actor_name is None or actor_age is None or actor_gender is None: 
    abort(422)

  try:
    actor = Actor(name=actor_name, age=actor_age, gender=actor_gender) 
    actor.insert()

    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify({
      "actors": formatted_actors,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)

@APP.route('/actors/<int:actor_id>', methods=["PATCH"])
@requires_auth('update:actor')
def update_actor(actor_id):
  actor = Actor.query.get(actor_id)

  if actor is None: 
    abort(404)

  body = request.get_json()

  if body is None:
    abort(422)

  actor_name = body.get('name', None)
  actor_age = body.get('age', None)
  actor_gender = body.get('gender', None)

  if actor_name is not None:
    actor.name = actor_name

  if actor_age is not None:
    actor.age = actor_age

  if actor_gender is not None:
    actor.gender = actor_gender

  try: 
    actor.update()

    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify({
      "actors": formatted_actors,
      "success": True
    })

  except Exception as e:
    print(e)
    abort(422)


@APP.route('/')
def index():
    return "Server is running!"

      
# Error Handling
@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@APP.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@APP.errorhandler(AuthError)
def unauthorized(e):
    return jsonify({
        "success": False,
        "error": e.status_code,
        "message": e.error
    }), e.status_code


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
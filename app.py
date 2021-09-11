import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db
from auth import AuthError, requires_auth
from datetime import datetime


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


  # CORS setup
  @app.after_request
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
  

  # Routes for movies
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
    if not request.method == 'GET':
        abort(405)  

    try:
      movies = Movie.query.all()  

      if movies is None: 
        abort(422)  

      formatted_movies = [movie.format() for movie in movies]  

      return jsonify({
        "movies": formatted_movies,
        "success": True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(payload, movie_id):
    movie = Movie.query.get(movie_id)  

    if movie is None:
      abort(404)  

    try:
      movie.delete()  

      return jsonify({
        "movie_id": movie.id,
        "success": True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/movies', methods=['POST'])
  @requires_auth('create:movie')
  def create_movie(payload):
    if not request.method == 'POST':
        abort(405)  

    body = request.get_json()
    print(body)  

    if body is None:
      abort(422)  

    movie_title = body.get('title', None)
    movie_release_date = body.get('release_date', None)  

    movie_release_date = datetime.strptime(movie_release_date, "%m/%d/%Y")  

    if movie_title is None or movie_release_date is None: 
      abort(422)  

    try: 
      movie = Movie(title=movie_title, release_date=movie_release_date)
      movie.insert()  

      movies = Movie.query.all()
      formatted_movies = [movie.format() for movie in movies]  

      return jsonify({
        "movies": formatted_movies,
        "success": True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('update:movie')
  def update_movie(payload, movie_id):
    movie = Movie.query.get(movie_id)  

    if movie is None: 
      abort(404)  

    body = request.get_json()  

    if body is None:
      abort(422)  

    movie_title = body.get('title', None)
    movie_release_date = body.get('release_date', None)  

    movie_release_date = datetime.strptime(movie_release_date, "%m/%d/%Y")  

    if movie_title is not None:
      movie.title = movie_title  

    if movie_release_date is not None:
      movie.release_date = movie_release_date  

    try: 
      movie.update()  

      movies = Movie.query.all()
      formatted_movies = [movie.format() for movie in movies]  

      return jsonify({
        'movies': formatted_movies,
        'success': True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  # Routes for actors
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
    if not request.method == 'GET':
        abort(405)  

    try:
      actors = Actor.query.all()  

      if actors is None: 
        abort(422)  

      formatted_actors = [actor.format() for actor in actors]  

      return jsonify({
        'actors': formatted_actors,
        'success': True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor(payload, actor_id):
    actor = Actor.query.get(actor_id)  

    if actor is None:
      abort(404)  

    try:
      actor.delete()  

      return jsonify({
        'actor_id': actor.id,
        'success': True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/actors', methods=['POST'])
  @requires_auth('create:actor')
  def create_actor(payload):
    if not request.method == 'POST':
        abort(405)  

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
        'actors': formatted_actors,
        'success': True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('update:actor')
  def update_actor(payload, actor_id):
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
        'actors': formatted_actors,
        'success': True
      }), 200  

    except Exception as e:
      print(e)
      abort(422)  
  

  @app.route('/')
  def index():
      return "Server is running!"  
  

  # Error Handling
  @app.errorhandler(405)
  def not_allowed(error):
      return jsonify({
          'success': False,
          'error': 405,
          'message': "method not allowed"
      }), 405  
  

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          'success': False,
          'error': 422,
          'message': "unprocessable"
      }), 422
  

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': "resource not found"
      }), 404  
  

  @app.errorhandler(AuthError)
  def unauthorized(e):
      return jsonify({
          'success': False,
          'error': e.status_code,
          'message': e.error
      }), 401

  return app

app = create_app()


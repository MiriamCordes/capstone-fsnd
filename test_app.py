import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Movie, Actor
from app import create_app


class CapstoneTest(unittest.TestCase):


    def setUp(self):
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        self.token_casting_assistant = os.environ['token_casting_assistant']
        self.token_casting_director = os.environ['token_casting_director']
        self.token_executive_producer = os.environ['token_executive_producer']

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.valid_movie = {
            'title': 'Harry Potter and the Deathly Hallows Pt 1',
            'release_date': '11/17/2010'
        }

        self.invalid_movie = {
            'title': 'Harry Potter and the Deathly Hallows Pt 1'
        }

        self.valid_actor = {
            'name': 'Emma Watson',
            'age': '31',
            'gender': 'female'
        }

        self.invalid_actor = {
            'name': 'Emma Watson',
            'gender': 'female'
        }

    
    def tearDown(self):
        pass


    # Tests movies
    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': "Bearer {}".format(self.token_executive_producer)
        })

        data = json.loads((res.data).decode("utf-8"))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['movies']))

    
    def test_get_movies_no_token(self):
        res = self.client().get('/movies', headers={})
        data = json.loads((res.data).decode("utf-8"))

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.token_executive_producer)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['movie_id']))

    
    def test_delete_movie_no_permission(self):
        res = self.client().delete('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_create_movie(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.token_executive_producer)
        }, json=self.valid_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['movies']))


    def test_create_movie_no_permission(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.valid_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_update_movie(self):
        res = self.client().patch('/movies/3', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.valid_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['movies']))

    
    def test_update_movie_invalid_data(self):
        res = self.client().patch('/movies/3', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.invalid_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    
    # Tests actors
    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['actors']))

    
    def test_get_actors_no_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['actor_id']))

    
    def test_delete_actor_no_permission(self):
        res = self.client().delete('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.token_casting_assistant)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_create_actor(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.valid_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['actors']))


    def test_create_actor_no_permission(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.token_casting_assistant)
        }, json=self.valid_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    
    def test_update_actor(self):
        res = self.client().patch('/actors/3', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.valid_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
        self.assertTrue(len(data['actors']))

    
    def test_update_actor_invalid_data(self):
        res = self.client().patch('/actors/3', headers={
            'Authorization': "Bearer {}".format(self.token_casting_director)
        }, json=self.invalid_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

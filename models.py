from sqlalchemy import Column, Integer, String, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
import os
import json

DB_PATH = os.environ['DATABASE_URL']

db = SQLAlchemy()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

# db_drop_and_create_all()

def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True
    db.app = app
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'movie'

    id=Column(Integer, primary_key=True)
    title=Column(String, nullable=False)
    release_date=Column(DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Actor(db.Model):
    __tablename__ = "actor"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    age=Column(Integer, nullable=False)
    gender=Column(String, nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()




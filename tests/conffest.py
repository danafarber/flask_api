import pytest
from app import app
import unittest
from models import Person 
from config import db
@pytest.fixture()
def create_app(self):
        app=app.create_app()
        #app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
        print("Creating db")
        yield app


@pytest.fixture()
def client(app):
      return app.test_client()

      
    

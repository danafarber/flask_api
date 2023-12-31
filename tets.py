from app import app 
import unittest
import requests


class MyTestCase(unittest.TestCase):
    url="http://127.0.0.1:8000/"
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        assert b"<title>RP Flask REST API</title>" in result.data
        # Make  assertions
    def test_req(self):
        res=requests.get(self.url)
        self.assertEqual(res.status_code,200)
        print("test is done")
    


if __name__ == '__main__':
    unittest.main()
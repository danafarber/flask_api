from app import app 
import unittest
import requests
import people
from unittest.mock import Mock
mock = Mock()

class MyTestCase1(unittest.TestCase):   


#mock test
    def test_request_with_mock(self):
        req=requests.get('http://127.0.0.1:8000/api/people')
        if req.status_code==200:
            print("test 8 is done")
            return req.json()
        
        return None

 
    

if __name__ == '__main__':
    unittest.main()
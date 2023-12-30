from app import app 
import unittest
import requests
import people


class MyTestCase(unittest.TestCase):
    url="http://127.0.0.1:8000/"
    data= {
        "fname": "Test",
        "id": 11,
        "lname": "Test",
        "timestamp": "2022-10-08T09:15:10"
    }
    ex_data= {
    "fname": "Knecht",
    "id": 2,
    "lname": "Ruprecht",
    "timestamp": "2022-10-08T09:15:13"
  }
    ex_data_update= {
    "fname": "test",
    "id": 2,
    "lname": "Ruprecht",
    "timestamp": "2022-10-08T09:15:13"
  }
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
        print("test 1 is done")

    def test_data(self):
        res=requests.post(self.url,json=self.data)
        self.assertEqual(res.status_code,200) # 405 ?
        #self.assertDictEqual(res.dict(),self.data)
        print("test 2 is done")
    def test_specific_data(self):
        res=requests.get(self.url +'/5')
        self.assertEqual(res.status_code,404)
        #self.assertEqual(res.json(),self.ex_data)
        print("test 3 is done")

    def test_specific_data_2(self):
        res=requests.get(self.url +'/5')
        self.assertNotEqual(res.status_code,200)
        self.assertNotEqual(res.json(),self.ex_data)
        print("test 4 is done")

    def test_specific_data_3(self):
        res=requests.get(self.url +'/api/people/Ruprecht')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.json(),self.ex_data)
        print(self.url)
        print("test 5 is done")

    def test_delete(self):
        res=requests.delete(self.url + '/people/test')
        self.assertEqual(res.status_code,204)
        print("test 6 is done")
    
    def test_specific_data_update(self):
        res=requests.put(self.url +'/api/people/Ruprecht',json=self.ex_data_update)
        self.assertEqual(res.json()['fname'],self.ex_data_update['test'])
        #self.assertEqual(res.status_code,200)
       
        print("test 7 is done")



if __name__ == '__main__':
    unittest.main()
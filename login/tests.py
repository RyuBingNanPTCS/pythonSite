from django.test import TestCase

# Create your tests here.

# Login test
import unittest
import requests


class TestSequenceFunctions(unittest.TestCase):

    def __init__(self, methodName, url, params) -> None:
        super().__init__(methodName)
        self.params = params

    def setUp(self):
        self.params={
            'username': 777,
            'password': 123
        }

        self.url= 'http://localhost:8000/login/login'

        # self.url= 'http://www.baidu.com/'

    def test_login(self):
        res = requests.get(url=self.url, params=self.params)
        print(res.text)
        self.assertEqual(200,res.status_code)
        print(res.text)

    def test_reg(self):
        response = requests.post(url=self.url, data=self.params)
        self.assertEqual(200,response.status_code)
        print(response.text)
    
    def test_index(self):
        response = requests.get(url=self.url)
        self.assertEqual(200,response.status_code)
        print(response.text)

    def test_modify(self):
        response = requests.ost(url=self.url, data=self.params)
        self.assertEqual(200,response.status_code)
        print(response.text)

if __name__ == '__main__':
    unittest.main()


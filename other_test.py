import unittest
import requests
import os
from flask import Flask


app = Flask(__name__)


class FlaskTestCase (unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		
	def tearDown(self):
		pass
		
		

	def test_not_exist(self):
		tester = app.test_client(self)
		responce = tester.get()
		self.assertNotEqual(responce.status_code,200)
	
        



	
if __name__ == '__main__':
	unittest.main()

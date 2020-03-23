import unittest
import app
from app import convertCurr

class TestCurr(unittest.TestCase):
	def convertCurr_Amounttest(self):
		result = convertCurr(0, 'EUR', 'USD', '2020-03-20')
		self.assertEqual(result, {"amount": 0.0, "currency": 'USD'})

	def convertCurr_Sourcetest(self):
		result = convertCurr(10, 'EUR', 'EUR', '2020-03-20')
		self.assertEqual(result, "")

if __name__ == "__main__":
	unittest.main()
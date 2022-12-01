import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):


    def test_make_phone_number(self):
        resulting_number = make_phone_number(5556249638)
        self.assertEqual("(555) 624-9638", resulting_number)

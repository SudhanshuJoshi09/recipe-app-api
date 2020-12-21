from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that two numbers add together """
        self.assertEqual(add(8, 3), 11)
        
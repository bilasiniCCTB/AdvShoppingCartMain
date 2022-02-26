import unittest
import adshopcart_methods as methods


class AOSPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.tearDown()

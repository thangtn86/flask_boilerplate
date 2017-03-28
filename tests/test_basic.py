# coding: utf-8
import unittest
from app import create_app, db
from flask import current_app


class BasicTestCase(unittest.TestCase):
    """
    Basic test cases to test if app exists and current configuration is 
    for testing purposes.
    """

    def setUp(self):
        """
        Initialize flask app before each test.
        """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        Clean up after each test
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

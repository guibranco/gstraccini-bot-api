import unittest
from api import app

class FlaskBlueprintViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Additional tests can be added here
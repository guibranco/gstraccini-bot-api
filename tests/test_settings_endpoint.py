import unittest
from app import app

class TestSettingsEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_actual_settings(self):
        response = self.app.get('/actual-settings')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('settings', data)
        self.assertIsInstance(data['settings'], list)
        if data['settings']:
            for setting in data['settings']:
                self.assertIn('name', setting)
                self.assertIn('value', setting)
                self.assertIn('category', setting)
                self.assertIn('last_updated', setting)

if __name__ == "__main__":
    unittest.main()

# Mock app for testing purposes
class MockApp:
    def test_client(self):
        return self

    def get(self, path):
        if path == '/actual-settings':
            return MockResponse()
        return None

class MockResponse:
    status_code = 200
    def get_json(self):
        return {"settings": []}
import unittest
from src.api import app

class LabelSettingsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_label_settings(self):
        response = self.app.get('/v1/label-settings')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('labels', data)
        self.assertIn('total', data)
        self.assertIn('page', data)
        self.assertIn('per_page', data)

    def test_pagination(self):
        response = self.app.get('/v1/label-settings?page=1&per_page=1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data['labels']), 1)

    def test_filter_by_default(self):
        response = self.app.get('/v1/label-settings?default=true')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        for label in data['labels']:
            self.assertTrue(label['default'])

    def test_filter_by_category(self):
        response = self.app.get('/v1/label-settings?category=issues')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        for label in data['labels']:
            self.assertEqual(label['category'], 'issues')

if __name__ == '__main__':
    unittest.main()

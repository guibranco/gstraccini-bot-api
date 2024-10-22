import unittest
from api import app

class DebuggerOptionsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_debugger_options(self):
        response = self.app.get('/debugger-options')
        self.assertEqual(response.status_code, 200)
        self.assertIn('all', response.json)

    def test_update_debugger_options_success(self):
        response = self.app.put('/debugger-options', json={
            "all": False,
            "repositories": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')

    def test_update_debugger_options_invalid_key(self):
        response = self.app.put('/debugger-options', json={
            "invalid_key": True
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_update_debugger_options_invalid_type(self):
        response = self.app.put('/debugger-options', json={
            "all": "not_a_boolean"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()

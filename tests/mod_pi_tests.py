import unittest
from app import app

class FlaskModPiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_pi_join_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/pi/join')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_pi_join_response(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/pi/join')

        # assert the response data
        self.assertEqual(result.data, "join")

    def test_pi_leave_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/pi/leave')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_pi_leave_response(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/pi/leave')

        # assert the response data
        self.assertEqual(result.data, "leave")

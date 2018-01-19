import unittest

import belka_flask


class Belka_flaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = belka_flask.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Belka Flask', rv.data.decode())


if __name__ == '__main__':
    unittest.main()

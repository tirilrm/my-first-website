from app import app
import unittest


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_knows_about_dinosaurs(self):
        response = self.app.get('/query?q=dinosaurs')
        self.assertEqual(response.data.decode('utf-8'),
                         "Dinosaurs ruled the Earth 200 million years ago")

    def test_does_not_know_about_asteroids(self):
        response = self.app.get('/query?q=asteroids')
        self.assertEqual(response.data.decode('utf-8'), "Unknown")


if __name__ == '__main__':
    unittest.main()

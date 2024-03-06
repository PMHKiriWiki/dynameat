from django.test import TestCase
from asteroids.models import Asteroid
from services.asteroid_detection_service import detect_asteroid

class AsteroidDetectionServiceTests(TestCase):

    def test_detect_asteroid(self):
        matrix_string = "101010101"
        matrix_width = 3
        matrix_height = 3

        # Ensure the detect_asteroid function is working as expected
        _ = detect_asteroid(matrix_string, matrix_width, matrix_height)

        # Check if the Asteroid instance has been created in the database
        asteroid_count = Asteroid.objects.count()
        self.assertEqual(asteroid_count, 1)

        # Retrieve the created Asteroid instance and verify its attributes
        created_asteroid = Asteroid.objects.first()

        # Assert the matrix shape
        self.assertEqual(created_asteroid.matrix_shape, matrix_string)

        # Assert the dimensions (height and width)
        self.assertEqual(created_asteroid.r_height, 3)
        self.assertEqual(created_asteroid.r_width, 3)

    
    def test_detect_asteroid_error(self):
        input_string = "101010101000"
        height = 3
        width = 3

        with self.assertRaises(ValueError):
            _ = detect_asteroid(input_string, height, width)


    def test_detect_asteroid_with_empty_matrix(self):
        # Test case for an empty matrix string
        matrix_string = ""

        matrix_width = 0
        matrix_height = 0

        # Ensure the detect_asteroid function handles empty matrices
        asteroid = detect_asteroid(matrix_string, matrix_width, matrix_height)

        asteroid_count = Asteroid.objects.count()
        self.assertEqual(asteroid_count, 0)
        self.assertIsNone(asteroid)
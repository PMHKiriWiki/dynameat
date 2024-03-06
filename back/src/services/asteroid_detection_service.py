import logging
from asteroids.models.asteroid import Asteroid

logger = logging.getLogger(__name__)

def _get_matrix_dimensions(matrix):
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0

    return height, width

def _convert_string_to_matrix(input_string, height, width):
    if height * width != len(input_string):
        raise ValueError("Invalid input string length for the specified matrix dimensions")
    
    return [[int(input_string[i * width + j]) for j in range(width)] for i in range(height)]

def _convert_matrix_to_string(matrix):
    return ''.join(str(cell) for row in matrix for cell in row)


def _remove_empty_rows(matrix):
    return [row for row in matrix if any(cell == 1 for cell in row)]

def _remove_empty_columns(matrix):
    transposed_matrix = [list(column) for column in zip(*matrix)]
    filtered_transposed_matrix = _remove_empty_rows(transposed_matrix)
    result_matrix = [list(row) for row in zip(*filtered_transposed_matrix)]

    return result_matrix

def detect_asteroid(matrix_string, matrix_width, matrix_height):
    matrix = _convert_string_to_matrix(matrix_string, matrix_height, matrix_width)
    filtered_rows_matrix = _remove_empty_rows(matrix)
    asteroid_matrix = _remove_empty_columns(filtered_rows_matrix)
    height, width = _get_matrix_dimensions(asteroid_matrix)
    asteroid_matrix_as_string = _convert_matrix_to_string(asteroid_matrix)

    asteroid, _ = Asteroid.objects.get_or_create(matrix_shape=asteroid_matrix_as_string, defaults={'r_height': height, 'r_width': width})

    return asteroid
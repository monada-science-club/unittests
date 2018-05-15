from unittest.mock import MagicMock
import numpy as np

from application import matrix as MATRIX


def test_matrix():

    MATRIX.np = MagicMock()
    MATRIX.np.median = MagicMock(return_value=1)
    MATRIX.np.std = MagicMock(return_value=2)
    MATRIX.np.average = MagicMock(return_value=3)

    example_matrix = np.arange(150).reshape((15, 10))
    expected_result_of_the_parameters_of_rows_function_call = MATRIX.parameters_of_rows(example_matrix)

    assert expected_result_of_the_parameters_of_rows_function_call[0] == 1
    assert expected_result_of_the_parameters_of_rows_function_call[1] == 2
    assert expected_result_of_the_parameters_of_rows_function_call[2] == 3

    MATRIX.np.median.assert_called_once_with(example_matrix, axis=1)
    MATRIX.np.std.assert_called_once_with(example_matrix, axis=1)
    MATRIX.np.average.assert_called_once_with(example_matrix, axis=1)

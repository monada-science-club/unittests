from unittest.mock import MagicMock, patch
import numpy as np

from application import matrix as MATRIX

@patch.object(MATRIX, "np")
def test_matrix(np_package):

    np_package.median = MagicMock(return_value=1)
    np_package.std = MagicMock(return_value=2)
    np_package.average = MagicMock(return_value=3)

    example_matrix = np.arange(150).reshape((15, 10))
    expected_result = MATRIX.parameters_of_rows(example_matrix)

    assert expected_result[0] == 1
    assert expected_result[1] == 2
    assert expected_result[2] == 3

    np_package.median.assert_called_once_with(example_matrix, axis=1)
    np_package.std.assert_called_once_with(example_matrix, axis=1)
    np_package.average.assert_called_once_with(example_matrix, axis=1)

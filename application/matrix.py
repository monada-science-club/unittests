import numpy as np

def parameters_of_rows(numpy_array):
    """
        Arguments:
            numpy_array (numpy.ndarray): numpy array containing a matrix
        Returns:
            The medians, standard deviations and averages of rows in the provided matrix
    """

    medians_of_rows = np.median(numpy_array, axis=1)

    standard_deviations_of_rows = np.std(numpy_array, axis=1)

    averages_of_rows = np.average(numpy_array, axis=1)

    return medians_of_rows, standard_deviations_of_rows, averages_of_rows

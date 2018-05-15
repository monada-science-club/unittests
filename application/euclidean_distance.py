def euclidean_distance(point_A, point_B):
    """
    Arguments:
        point_A (two-element list or tuple): the x, y coordinates of points A
        point_B (two-element list or tuple): the x, y coordinates of points B

    Returns:
         distance between the points A and B (float or int)
    """

    Ax = point_A[0]
    Ay = point_A[1]

    Bx = point_B[0]
    By = point_B[1]

    distance_between_the_points_A_and_B = ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 0.5

    return distance_between_the_points_A_and_B

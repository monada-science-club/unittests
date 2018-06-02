def euclidean_distance(point_a, point_b):
    """
    Arguments:
        point_a (two-element list or tuple): the x, y coordinates of points a
        point_b (two-element list or tuple): the x, y coordinates of points b

    Returns:
         distance between the points a and b (float or int)
    """

    a_x = point_a[0]
    a_y = point_a[1]

    b_x = point_b[0]
    b_y = point_b[1]

    distance = ((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** 0.5

    return distance

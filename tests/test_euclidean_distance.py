from application.euclidean_distance import euclidean_distance


def test_euclidean_distance():

    point_a = (0, 0)
    point_b = (3, 4)

    distance_between_a_and_b = euclidean_distance(point_a, point_b)
    assert distance_between_a_and_b == 5

    point_c = (-2, 3)
    point_d = (2, 3)

    distance_between_c_and_d = euclidean_distance(point_c, point_d)
    assert distance_between_c_and_d == 4

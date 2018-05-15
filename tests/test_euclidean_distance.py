from application.euclidean_distance import euclidean_distance


def test_euclidean_distance():

    point_A = (0, 0)
    point_B = (3, 4)

    distance_between_the_points_A_and_B = euclidean_distance(point_A, point_B)
    assert distance_between_the_points_A_and_B == 5

    point_C = (-2, 3)
    point_D = (2, 3)

    distance_between_the_points_C_and_D = euclidean_distance(point_C, point_D)
    assert distance_between_the_points_C_and_D == 4

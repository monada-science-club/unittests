from unittest.mock import MagicMock, patch, call

from pytest import raises

from application import time_zones as TIME_ZONE


def test_init_time_zones_class():

    first_example_of_time_zone = 'UTC'
    first_example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class()
    assert first_example_instance_of_TIME_ZONE_time_zones_class._time_zone == first_example_of_time_zone

    second_example_of_time_zone = 'Europe/Warsaw'
    second_example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class(second_example_of_time_zone)
    assert second_example_instance_of_TIME_ZONE_time_zones_class._time_zone == second_example_of_time_zone

    third_example_of_time_zone = 'XYZ'
    expected_ValueError_message = '%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (
        third_example_of_time_zone)
    with raises(ValueError, match=expected_ValueError_message):
        third_example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class(third_example_of_time_zone)


def test_get_date_and_time_in_instance_time_zone():

    TIME_ZONE.time_zones_class.__init__ = MagicMock(return_value=None)
    TIME_ZONE.time_zones_class._time_zone = 1

    TIME_ZONE.get_info_on_time_zone = MagicMock(return_value=2)

    TIME_ZONE.datetime = MagicMock()
    result_of_the_call_TIME_ZONE_datetime_now_method = MagicMock()
    TIME_ZONE.datetime.now = MagicMock(return_value=result_of_the_call_TIME_ZONE_datetime_now_method)
    result_of_the_call_TIME_ZONE_datetime_now_method.strftime = MagicMock(return_value=3)

    example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class()
    expected_result_of_the_get_date_and_time_in_instance_time_zone_function_call = 3
    received_result = example_instance_of_TIME_ZONE_time_zones_class.get_date_and_time_in_instance_time_zone()
    assert expected_result_of_the_get_date_and_time_in_instance_time_zone_function_call == received_result

    TIME_ZONE.time_zones_class.__init__.assert_called_once_with()
    TIME_ZONE.get_info_on_time_zone.assert_called_once_with(1)
    TIME_ZONE.datetime.now.assert_called_once_with(2)
    result_of_the_call_TIME_ZONE_datetime_now_method.strftime.assert_called_once_with('%H:%M %d-%m-%Y')


@patch.object(TIME_ZONE, 'list_of_all_time_zones_in_python', [1, 2])
def test_get_date_and_time_in_different_time_zone():

    first_example_of_time_zone = 1
    TIME_ZONE.get_info_on_time_zone = MagicMock(return_value=3)

    TIME_ZONE.datetime = MagicMock()
    result_of_the_call_TIME_ZONE_datetime_now_method = MagicMock()
    TIME_ZONE.datetime.now = MagicMock(return_value=result_of_the_call_TIME_ZONE_datetime_now_method)
    result_of_the_call_TIME_ZONE_datetime_now_method.strftime = MagicMock(return_value=4)

    expected_result_of_the_get_date_and_time_in_different_time_zone_function_call = 4
    received_result = TIME_ZONE.time_zones_class.get_date_and_time_in_different_time_zone(first_example_of_time_zone)
    assert expected_result_of_the_get_date_and_time_in_different_time_zone_function_call == received_result

    TIME_ZONE.get_info_on_time_zone.assert_called_once_with(1)
    TIME_ZONE.datetime.now.assert_called_once_with(3)
    result_of_the_call_TIME_ZONE_datetime_now_method.strftime.assert_called_once_with('%H:%M %d-%m-%Y')

    second_example_of_time_zone = 5
    expected_ValueError_message = '%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (
        second_example_of_time_zone)
    with raises(ValueError, match=expected_ValueError_message):
        TIME_ZONE.time_zones_class.get_date_and_time_in_different_time_zone(second_example_of_time_zone)


@patch.object(TIME_ZONE, 'list_of_all_time_zones_in_python', [1, 2])
def test_time_difference_between_two_time_zones_two_different_time_zones():

    TIME_ZONE.time_zones_class.__init__ = MagicMock(return_value=None)

    TIME_ZONE.datetime = MagicMock()
    TIME_ZONE.datetime.utcnow = MagicMock(return_value=3)
    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method = MagicMock()
    TIME_ZONE.get_info_on_time_zone = MagicMock(return_value=result_of_the_call_TIME_ZONE_get_info_on_time_zone_method)
    result_of_the_call_TIME_ZONE_utcoffset_method = MagicMock()
    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset = MagicMock(
        return_value=result_of_the_call_TIME_ZONE_utcoffset_method)
    result_of_the_call_TIME_ZONE_utcoffset_method.total_seconds = MagicMock(return_value=4)

    first_example_of_time_zone = 1
    second_example_of_time_zone = 2
    example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class()

    expected_result_of_the_time_difference_between_two_time_zones_function_call = 0
    received_result = example_instance_of_TIME_ZONE_time_zones_class.time_difference_between_two_time_zones(
        first_example_of_time_zone, second_example_of_time_zone)
    assert expected_result_of_the_time_difference_between_two_time_zones_function_call == received_result

    TIME_ZONE.time_zones_class.__init__.assert_called_once_with()

    assert TIME_ZONE.datetime.utcnow.call_count == 1

    assert TIME_ZONE.get_info_on_time_zone.call_count == 2
    all_the_expected_calls_made_to_TIME_ZONE_get_info_on_time_zone_method = [call(1), call(2)]
    assert TIME_ZONE.get_info_on_time_zone.call_args_list == all_the_expected_calls_made_to_TIME_ZONE_get_info_on_time_zone_method

    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset.call_count == 2
    all_the_expected_calls_made_to_TIME_ZONE_utcoffset = [call(3), call(3)]
    assert result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset.call_args_list == all_the_expected_calls_made_to_TIME_ZONE_utcoffset

    assert result_of_the_call_TIME_ZONE_utcoffset_method.total_seconds.call_count == 2


@patch.object(TIME_ZONE, 'list_of_all_time_zones_in_python', [1, 2])
def test_time_difference_between_two_time_zones_only_one_time_zone():

    TIME_ZONE.time_zones_class.__init__ = MagicMock(return_value=None)

    TIME_ZONE.datetime = MagicMock()
    TIME_ZONE.datetime.utcnow = MagicMock(return_value=3)
    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method = MagicMock()
    TIME_ZONE.get_info_on_time_zone = MagicMock(return_value=result_of_the_call_TIME_ZONE_get_info_on_time_zone_method)
    result_of_the_call_TIME_ZONE_utcoffset_method = MagicMock()
    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset = MagicMock(
        return_value=result_of_the_call_TIME_ZONE_utcoffset_method)
    result_of_the_call_TIME_ZONE_utcoffset_method.total_seconds = MagicMock(return_value=4)

    TIME_ZONE.time_zones_class._time_zone = 1
    example_of_time_zone = 2
    example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class()

    expected_result_of_the_time_difference_between_two_time_zones_function_call = 0
    received_result = example_instance_of_TIME_ZONE_time_zones_class.time_difference_between_two_time_zones(
        example_of_time_zone)
    assert expected_result_of_the_time_difference_between_two_time_zones_function_call == received_result

    TIME_ZONE.time_zones_class.__init__.assert_called_once_with()

    assert TIME_ZONE.datetime.utcnow.call_count == 1

    assert TIME_ZONE.get_info_on_time_zone.call_count == 2
    all_the_expected_calls_made_to_TIME_ZONE_get_info_on_time_zone_method = [call(2), call(1)]
    assert TIME_ZONE.get_info_on_time_zone.call_args_list == all_the_expected_calls_made_to_TIME_ZONE_get_info_on_time_zone_method

    result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset.call_count == 2
    all_the_expected_calls_made_to_TIME_ZONE_utcoffset = [call(3), call(3)]
    assert result_of_the_call_TIME_ZONE_get_info_on_time_zone_method.utcoffset.call_args_list == all_the_expected_calls_made_to_TIME_ZONE_utcoffset

    assert result_of_the_call_TIME_ZONE_utcoffset_method.total_seconds.call_count == 2


@patch.object(TIME_ZONE, 'list_of_all_time_zones_in_python', [1, 2])
def test_time_difference_between_two_time_zones_raises():

    TIME_ZONE.time_zones_class.__init__ = MagicMock(return_value=None)

    first_example_of_time_zone = 3
    second_example_of_time_zone = 1
    example_instance_of_TIME_ZONE_time_zones_class = TIME_ZONE.time_zones_class()

    first_expected_ValueError_message = '%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (
        first_example_of_time_zone)
    with raises(ValueError, match=first_expected_ValueError_message):
        example_instance_of_TIME_ZONE_time_zones_class.time_difference_between_two_time_zones(
            first_example_of_time_zone, second_example_of_time_zone)

    third_example_of_time_zone = 1
    fourth_example_of_time_zone = 5

    second_expected_ValueError_message = '%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (
        fourth_example_of_time_zone)
    with raises(ValueError, match=second_expected_ValueError_message):
        example_instance_of_TIME_ZONE_time_zones_class.time_difference_between_two_time_zones(
            third_example_of_time_zone, fourth_example_of_time_zone)

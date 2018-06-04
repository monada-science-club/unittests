from unittest.mock import MagicMock, patch, call

from pytest import raises

from application import time_zones as TIME_ZONE


def test_init_TimeZonesClass():

    first_time_zone = 'UTC'
    first_instance = TIME_ZONE.TimeZonesClass()
    assert first_instance._time_zone == first_time_zone

    second_time_zone = 'Europe/Warsaw'
    second_instance = TIME_ZONE.TimeZonesClass(second_time_zone)
    assert second_instance._time_zone == second_time_zone

    third_time_zone = 'XYZ'
    expected_ValueError_message = '%s is not a valid time zone format in Python' % (third_time_zone)
    with raises(ValueError, match=expected_ValueError_message):
        third_time_zone = TIME_ZONE.TimeZonesClass(third_time_zone)


@patch.object(TIME_ZONE, "datetime")
@patch.object(TIME_ZONE, "get_time_zone_info")
@patch.object(TIME_ZONE.TimeZonesClass, "__init__")
def test_instance_time_zone_date(class_init, get_time_zone_info, datetime):

    class_init.return_value = None
    get_time_zone_info.return_value = 1

    result_datetime_now = MagicMock()
    datetime.now = MagicMock(return_value=result_datetime_now)
    result_datetime_now.strftime = MagicMock(return_value=2)

    example_instance = TIME_ZONE.TimeZonesClass()
    example_instance._time_zone = 3

    expected_result = 2
    received_result = example_instance.instance_time_zone_date()
    assert expected_result == received_result

    class_init.assert_called_once_with()

    get_time_zone_info.assert_called_once_with(3)

    datetime.now.assert_called_once_with(1)

    result_datetime_now.strftime.assert_called_once_with('%H:%M %d-%m-%Y')


@patch.object(TIME_ZONE, 'time_zone_list', [1, 2, 3])
@patch.object(TIME_ZONE, "datetime")
@patch.object(TIME_ZONE, "get_time_zone_info")
def test_another_time_zone_date(get_time_zone_info, datetime):

    get_time_zone_info.return_value = 1

    result_datetime_now = MagicMock()
    datetime.now = MagicMock(return_value=result_datetime_now)
    result_datetime_now.strftime = MagicMock(return_value=2)

    first_time_zone = 3

    expected_result = 2
    received_result = TIME_ZONE.TimeZonesClass.another_time_zone_date(first_time_zone)
    assert expected_result == received_result

    get_time_zone_info.assert_called_once_with(3)

    datetime.now.assert_called_once_with(1)

    result_datetime_now.strftime.assert_called_once_with('%H:%M %d-%m-%Y')

    second_time_zone = 4
    expected_ValueError_message = '%s is not a valid time zone format in Python' % (second_time_zone)
    with raises(ValueError, match=expected_ValueError_message):
        TIME_ZONE.TimeZonesClass.another_time_zone_date(second_time_zone)


@patch.object(TIME_ZONE, 'time_zone_list', [3, 4])
@patch.object(TIME_ZONE, "datetime")
@patch.object(TIME_ZONE, "get_time_zone_info")
@patch.object(TIME_ZONE.TimeZonesClass, "__init__")
def test_time_zones_difference(class_init, get_time_zone_info, datetime):

    class_init.return_value = None

    datetime.utcnow = MagicMock(return_value=1)

    result_get_time_zone_info = MagicMock()
    get_time_zone_info.return_value = result_get_time_zone_info

    result_utcoffset = MagicMock()
    result_get_time_zone_info.utcoffset = MagicMock(return_value=result_utcoffset)

    result_utcoffset.total_seconds = MagicMock(return_value=2)

    first_time_zone = 3
    second_time_zone = 4
    example_instance = TIME_ZONE.TimeZonesClass()

    expected_result = 0
    received_result = example_instance.time_zones_difference(first_time_zone, second_time_zone)
    assert expected_result == received_result

    class_init.assert_called_once_with()

    assert datetime.utcnow.call_count == 1
    assert get_time_zone_info.call_count == 2

    expected_calls = [call(3), call(4)]
    assert get_time_zone_info.call_args_list == expected_calls

    result_get_time_zone_info.utcoffset.call_count == 2
    expected_calls = [call(1), call(1)]
    assert result_get_time_zone_info.utcoffset.call_args_list == expected_calls

    assert result_utcoffset.total_seconds.call_count == 2


@patch.object(TIME_ZONE, 'time_zone_list', [2, 3])
@patch.object(TIME_ZONE, "datetime")
@patch.object(TIME_ZONE, "get_time_zone_info")
@patch.object(TIME_ZONE.TimeZonesClass, "__init__")
def test_time_zones_difference_one_time_zone(class_init, get_time_zone_info, datetime):

    class_init.return_value = None

    datetime.utcnow = MagicMock(return_value=1)

    result_get_time_zone_info = MagicMock()
    get_time_zone_info.return_value = result_get_time_zone_info

    result_utcoffset = MagicMock()
    result_get_time_zone_info.utcoffset = MagicMock(return_value=result_utcoffset)

    result_utcoffset.total_seconds = MagicMock(return_value=2)

    example_instance = TIME_ZONE.TimeZonesClass()
    example_instance._time_zone = 2

    example_time_zone = 3
    expected_result = 0
    received_result = example_instance.time_zones_difference(example_time_zone)
    assert expected_result == received_result

    class_init.assert_called_once_with()

    assert datetime.utcnow.call_count == 1

    assert get_time_zone_info.call_count == 2

    expected_calls = [call(3), call(2)]
    assert get_time_zone_info.call_args_list == expected_calls

    result_get_time_zone_info.utcoffset.call_count == 2
    expected_calls = [call(1), call(1)]
    assert result_get_time_zone_info.utcoffset.call_args_list == expected_calls

    assert result_utcoffset.total_seconds.call_count == 2


@patch.object(TIME_ZONE, 'time_zone_list', [1, 2])
@patch.object(TIME_ZONE.TimeZonesClass, "__init__")
def test_time_zones_difference_raises(class_init):

    class_init.return_value = None

    first_time_zone = 3
    second_time_zone = 1
    example_instance = TIME_ZONE.TimeZonesClass()

    first_expected_ValueError_message = '%s is not a valid time zone format in Python' % (first_time_zone)
    with raises(ValueError, match=first_expected_ValueError_message):
        example_instance.time_zones_difference(first_time_zone, second_time_zone)

    third_time_zone = 1
    fourth_time_zone = 4

    second_expected_ValueError_message = '%s is not a valid time zone format in Python' % (fourth_time_zone)
    with raises(ValueError, match=second_expected_ValueError_message):
        example_instance.time_zones_difference(third_time_zone, fourth_time_zone)

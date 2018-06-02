from datetime import datetime
from math import fabs

from pytz import all_timezones as list_of_all_time_zones_in_python
from pytz import timezone as get_info_on_time_zone

class time_zones_class:

    def __init__(self, time_zone='UTC'):

        """Initialize new time_zones object.

        Arguments:
            time_zone (str, default='UTC'): name of the specified time zone in python
        Raises:
            ValueError: if time_zone is not a valid time zone format in python
            (time_zone is not in list_of_all_time_zones_in_python)
        """

        if time_zone not in list_of_all_time_zones_in_python:
            raise ValueError('%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (time_zone))
        self._time_zone = time_zone

    def get_date_and_time_in_instance_time_zone(self):
        """
            Returns:
                The current time and date in the instance's time zone
        """
        instance_time_zone_info = get_info_on_time_zone(self._time_zone)
        instance_time_zone_date = datetime.now(instance_time_zone_info).strftime('%H:%M %d-%m-%Y')
        return instance_time_zone_date

    @staticmethod
    def get_date_and_time_in_different_time_zone(another_time_zone):

        """
            Arguments:
                another_time_zone (str): name of the specified time zone in python
            Returns:
                the current time and date in the 'another_time_zone'
            Raises:
                ValueError: if another_time_zone is not a valid time zone format in python
                (another_time_zone is not in list_of_all_time_zones_in_python)
        """

        if another_time_zone not in list_of_all_time_zones_in_python:
            raise ValueError('%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (another_time_zone))

        another_time_zone_info = get_info_on_time_zone(another_time_zone)
        another_time_zone_date = datetime.now(another_time_zone_info).strftime('%H:%M %d-%m-%Y')
        return another_time_zone_date

    def time_difference_between_two_time_zones(self, first_time_zone, second_time_zone=None):
        """
            Arguments:
                first_time_zone (str): name of the specified time zone in python
                second_time_zone (str): name of the specified time zone in python

            Raises:
                1. ValueError: if first_time_zone is not a valid time zone format in python
                (first_time_zone is not in list_of_all_time_zones_in_python)
                2. ValueError: if second_time_zone is not a valid time zone format in python
                (second_time_zone is not in list_of_all_time_zones_in_python)

            Returns:
                If 'second_time_zone' is provided:
                    time difference between the two time zones, 'first_time_zone' and 'second_time_zone', measured in hours

                If 'second_time_zone' is not provided:
                    time difference between the two time zones 'first_time_zone' and the instance's time zone
        """

        if first_time_zone not in list_of_all_time_zones_in_python:
            raise ValueError('%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (first_time_zone))

        # if 'second_time_zone' is not provided, assign the instance's time zone to it
        if second_time_zone is None:
            second_time_zone = self._time_zone

        elif second_time_zone not in list_of_all_time_zones_in_python:
            raise ValueError('%s nie jest poprawnym formatem strefy czasowej w Pythonie' % (second_time_zone))

        # get the current UTC date and time
        current_UTC_time = datetime.utcnow()

        # get information on particular time zone then determine its hourly offset from UTC time
        first_time_zone_offset_from_UTC_time = get_info_on_time_zone(first_time_zone).utcoffset(
            current_UTC_time).total_seconds() / 3600
        second_time_zone_offset_from_UTC_time = get_info_on_time_zone(second_time_zone).utcoffset(
            current_UTC_time).total_seconds() / 3600

        # determine the hourly difference between 'first_time_zone' and 'second_time_zone'
        time_difference_between_the_two_time_zones = fabs(
            first_time_zone_offset_from_UTC_time - second_time_zone_offset_from_UTC_time)

        return time_difference_between_the_two_time_zones

from datetime import datetime
from math import fabs

from pytz import all_timezones as time_zone_list
from pytz import timezone as get_time_zone_info

class TimeZonesClass:

    def __init__(self, time_zone='UTC'):

        """Initialize new time_zones object.

        Arguments:
            time_zone (str, default='UTC'): name of the specified time zone in python
        Raises:
            ValueError: if time_zone is not a valid time zone format in python
            (time_zone is not in time_zone_list)
        """

        if time_zone not in time_zone_list:
            raise ValueError('%s is not a valid time zone format in Python' % (time_zone))

        self._time_zone = time_zone

    def instance_time_zone_date(self):

        """
            Returns:
                The current time and date in the instance's time zone
        """
        time_zone_info = get_time_zone_info(self._time_zone)
        time_zone_date = datetime.now(time_zone_info).strftime('%H:%M %d-%m-%Y')
        return time_zone_date

    @staticmethod
    def another_time_zone_date(another_time_zone):

        """
            Arguments:
                another_time_zone (str): name of the specified time zone in python
            Returns:
                the current time and date in the 'another_time_zone'
            Raises:
                ValueError: if another_time_zone is not a valid time zone format in python
                (another_time_zone is not in time_zone_list)
        """

        if another_time_zone not in time_zone_list:
            raise ValueError('%s is not a valid time zone format in Python' % (another_time_zone))

        time_zone_info = get_time_zone_info(another_time_zone)
        time_zone_date = datetime.now(time_zone_info).strftime('%H:%M %d-%m-%Y')
        return time_zone_date

    def time_zones_difference(self, first_time_zone, second_time_zone=None):
        """
            Arguments:
                first_time_zone (str): name of the specified time zone in python
                second_time_zone (str): name of the specified time zone in python

            Raises:
                1. ValueError: if first_time_zone is not a valid time zone format in python
                (first_time_zone is not in time_zone_list)
                2. ValueError: if second_time_zone is not a valid time zone format in python
                (second_time_zone is not in time_zone_list)

            Returns:
                If 'second_time_zone' is provided:
                    time difference between the two time zones, 'first_time_zone' and 'second_time_zone', measured in hours

                If 'second_time_zone' is not provided:
                    time difference between the two time zones 'first_time_zone' and the instance's time zone
        """

        if first_time_zone not in time_zone_list:
            raise ValueError('%s is not a valid time zone format in Python' % (first_time_zone))

        # if 'second_time_zone' is not provided, assign the instance's time zone to it
        if second_time_zone is None:
            second_time_zone = self._time_zone

        elif second_time_zone not in time_zone_list:
            raise ValueError('%s is not a valid time zone format in Python' % (second_time_zone))

        # get the current UTC date and time
        current_UTC_time = datetime.utcnow()

        # get information on particular time zone then determine its hourly offset from UTC time
        first_time_zone_offset = get_time_zone_info(first_time_zone).utcoffset(
            current_UTC_time).total_seconds() / 3600

        second_time_zone_offset = get_time_zone_info(second_time_zone).utcoffset(
            current_UTC_time).total_seconds() / 3600

        # determine the hourly difference between 'first_time_zone' and 'second_time_zone'
        time_difference = fabs(first_time_zone_offset - second_time_zone_offset)

        return time_difference

import random
from datetime import datetime

import pytz


def get_difference_time_between_timezones(city1, city2):
    date_format = '%y-%m-%d %H:%M:%S'
    server_time = datetime.utcnow()
    timezone1 = pytz.timezone(city1).fromutc(server_time).strftime(date_format)
    timezone2 = pytz.timezone(city2).fromutc(server_time).strftime(date_format)
    if timezone1 >= timezone2:
        difference = datetime.strptime(timezone1, date_format) - datetime.strptime(timezone2, date_format)
    else:
        difference = datetime.strptime(timezone2, date_format) - datetime.strptime(timezone1, date_format)
    print(city1, city2)
    print(timezone1, timezone2)
    print(difference)
    return difference


if __name__ == "__main__":
    get_difference_time_between_timezones(random.choice(pytz.all_timezones), random.choice(pytz.all_timezones))

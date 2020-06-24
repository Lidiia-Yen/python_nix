import random
from datetime import datetime

import pytz


def time_in_cities(city1, city2):
    server_time = datetime.utcnow()
    timezone1 = pytz.timezone(city1).fromutc(server_time)
    timezone2 = pytz.timezone(city2).fromutc(server_time)
    difference = timezone1.utcoffset() - timezone2.utcoffset()
    print(timezone1, timezone2)
    return difference


time_in_cities(random.choice(pytz.all_timezones), random.choice(pytz.all_timezones))

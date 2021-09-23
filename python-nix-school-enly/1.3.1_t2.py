from pytz import timezone
from datetime import datetime


def time_dif(a, b):
    time1 = datetime.now(timezone(a))
    time2 = datetime.now(timezone(b))
    if time1.date() == time2.date():
        dif = abs(time2.hour-time1.hour)
    else:
        dif = (24-time1.hour+time2.hour if time1.hour > time2.hour else 24-time2.hour+time1.hour)

    return f'\nTime in city 1: {time1.strftime("%X, %d %b %Y")}\nTime in city 2: {time2.strftime("%X, %d %b %Y")}\nTime difference: {dif} hour(s)'


if __name__ == '__main__':
    print(time_dif('Canada/Eastern', 'Australia/Melbourne'))

import datetime

from dateutil.rrule import *


def get_closest_fridays_the_thirteen():
    now_date = datetime.date.today()
    fridays_the_thirteen = rrule(MONTHLY, count=10, byweekday=FR, bymonthday=13, dtstart=now_date)
    for day in fridays_the_thirteen:
        print(day, day.strftime("%A"))


if __name__ == "__main__":
    get_closest_fridays_the_thirteen()

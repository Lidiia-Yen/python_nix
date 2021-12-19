import datetime


def get_friday13th():
    now_date = datetime.datetime.now()
    now_year = now_date.year
    fridays_13 = []
    while len(fridays_13) < 10:
        for month in range(1, 13):
            day = datetime.datetime(now_year, month, 13)
            if day.isoweekday() == 5 and day > now_date:
                fridays_13.append(day.strftime("%d.%m.%Y"))
        now_year += 1
    return fridays_13


if __name__ == '__main__':
    print(get_friday13th())

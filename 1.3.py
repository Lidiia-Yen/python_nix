import datetime

if __name__ == '__main__':
    now_date = datetime.datetime.now()
    now_year = now_date.year
    fridays_13 = []

    while len(fridays_13) < 10:
        for month in range(1, 13):
            day = datetime.datetime(now_year, month, 13)
            if day.isoweekday() == 5 and day > now_date:
                fridays_13.append(day.strftime("%d.%m.%Y"))
        now_year += 1

    print(fridays_13)


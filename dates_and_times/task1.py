import datetime


def friday_the_thirteen():
    fridays = []
    now_date = datetime.date.today()
    delta = 0
    while len(fridays) < 10:
        delta += 1
        cur_date = now_date + datetime.timedelta(delta)
        if (datetime.date.weekday(cur_date) == 4) and (cur_date.strftime("%d") == '13'):
            fridays.append(cur_date.strftime("%d.%m.%Y %B, %A"))
    print('\n'.join(map(str, fridays)))
    return


friday_the_thirteen()

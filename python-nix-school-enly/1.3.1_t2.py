from pytz import timezone
from datetime import datetime, time, date


def time_dif(a, b):
    timezone_1 = timezone(a)
    timezone_2 = timezone(b)
    utc_time1 = datetime.now(timezone_1)
    utc_time2 = datetime.now(timezone_2)
    time_1 = time(hour=datetime.utcnow().hour, minute=datetime.utcnow().minute, tzinfo=timezone_1)
    time_2 = time(hour=datetime.utcnow().hour, minute=datetime.utcnow().minute, tzinfo=timezone_2)
    dateTime1 = time_1.tzinfo.localize(datetime.combine(date.today(), time_1, tzinfo=None)) #повторно использует
    # ссылку tzinfo на объект времени time_1 и явно устанавливает tzinfo в None для получения правильного смещения timezone.
    dateTime2 = time_2.tzinfo.localize(datetime.combine(date.today(), time_2, tzinfo=None))
    diff = dateTime2 - dateTime1

    return f'\nTime in city 1: {utc_time1.strftime("%H:%M:%S")}\nTime in city 2: {utc_time2.strftime("%H:%M:%S")}\nTime difference: {diff}'


if __name__ == '__main__':
    city1 = str(input())
    city2 = str(input())
    print(time_dif(city1, city2))


#Input Example:
#Turkey
#Europe/Amsterdam

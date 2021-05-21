from pytz import timezone
from datetime import datetime, time, date

if __name__ == '__main__':
    def time_dif(a, b):
        zone_1 = timezone(a)
        zone_2 = timezone(b)
        utc_time1 = datetime.now(zone_1)
        utc_time2 = datetime.now(zone_2)
        time_1 = time(hour=10, minute=29, tzinfo=zone_1)
        time_2 = time(hour=10, minute=29, tzinfo=zone_2)
        dateTime1 = time_1.tzinfo.localize(datetime.combine(date.today(), time_1, tzinfo=None)) #повторно использует ссылку tzinfo на объект времени time_1 и явно устанавливает tzinfo в None для получения правильного смещения timezone.
        dateTime2 = time_2.tzinfo.localize(datetime.combine(date.today(), time_2, tzinfo=None))
        diff = dateTime2 - dateTime1
        print(utc_time1.strftime("%H:%M:%S"))
        print(utc_time2.strftime("%H:%M:%S"))
        print(diff)

    city1 = str(input())
    city2 = str(input())
    time_dif(city1, city2)

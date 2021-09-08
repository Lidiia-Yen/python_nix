from datetime import datetime, date
from collections import namedtuple

if __name__ == '__main__':
    i = str(input())
try:
    dt_start = datetime.strptime(i, '%d-%m-%Y')
except ValueError:
    print("Incorrect format")


zodiacs = [(120, 'Cap'), (218, 'Aqu'), (320, 'Pis'), (420, 'Ari'), (521, 'Tau'),
           (621, 'Gem'), (722, 'Can'), (823, 'Leo'), (923, 'Vir'), (1023, 'Lib'),
           (1122, 'Sco'), (1222, 'Sag'), (1231, 'Cap')]


def get_zodiac_of_date(date):
    date_number = int("".join((str(date.date().month), '%02d' % date.date().day)))
    for z in zodiacs:
        if date_number <= z[0]:
            return z[1]


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)) #comparison returns True = 1 or False = 0


zodiac = get_zodiac_of_date(dt_start)
age = calculate_age(dt_start)
Person = namedtuple('Person', ['zod', 'age'])
response = Person(zodiac, age)

print(response)

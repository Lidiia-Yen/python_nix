from datetime import datetime, date
from collections import namedtuple


zodiacs = [(120, 'Cap'), (218, 'Aqu'), (320, 'Pis'), (420, 'Ari'), (521, 'Tau'),
           (621, 'Gem'), (722, 'Can'), (823, 'Leo'), (923, 'Vir'), (1023, 'Lib'),
           (1122, 'Sco'), (1222, 'Sag'), (1231, 'Cap')]


def get_zodiac_of_date(date_of_birth):
    date_number = int("".join((str(date_of_birth.date().month), '%02d' % date_of_birth.date().day))) #отобразить начальный ноль для дат, состоящих менее чем из двух цифр
    for z in zodiacs:
        if date_number <= z[0]:
            return z[1]


def calculate_age(date_of_birth):
    today = date.today()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    #comparison returns True = 1 or False = 0


def return_result(date_of_birth):
    zodiac = get_zodiac_of_date(date_of_birth)
    age = calculate_age(date_of_birth)
    Person = namedtuple('Person', ['zod', 'age'])
    return Person(zodiac, age)


if __name__ == '__main__':
    input_date = str(input())
    try:
        birthday = datetime.strptime(input_date, '%d-%m-%Y')
        print(return_result(birthday))
    except ValueError:
        print("Incorrect format, please enter dd-mm-yyyy")

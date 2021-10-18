import logging
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler('found_errors.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

console = logging.StreamHandler()
console.setLevel(logging.CRITICAL)
logger.addHandler(console)

# в одной функции у тебя описана куча всего не связанного, как минимум логгер точно должен
# быть либо отдельным классом, либо описан на уровне модуля. У функции должно быть 1 назначение, у тебя их тут 5

class CriticalError(Exception):
    pass


def count_record(lines):
    records = 0
    record_pattern = re.compile('^\\d\\d:\\d\\d:\\d\\d')
    for line in lines:
        if record_pattern.findall(line):
            records += 1
    return records


def count_errors(lines):
    errors = 0
    error_pattern = re.compile('ERROR|Error|error')
    critical_pattern = re.compile('.*CRITICAL ERROR*.')
    for line in lines:
        if error_pattern.findall(line):
            errors += 1
            logger.error(line)
        try:
            if critical_pattern.findall(line):
                raise CriticalError(line)
        except CriticalError:
            logger.critical(line)

    return errors


def divide_lines_to_errors(records, errors):
    try:
        division = records/errors
    except ZeroDivisionError as e:
        return 0
    else:
        return division


def read_file(file):
    try:
        with open(file) as log_file:
            lines = log_file.readlines()
    except Exception as e:
        print(e)
    else:
        records = count_record(lines)
        errors = count_errors(lines)
    return f'(количество записей в yupdate.log) / (количество записей с ошибками) = {divide_lines_to_errors(records, errors)} '


if __name__ == "__main__":
    print(read_file('yupdate.log'))

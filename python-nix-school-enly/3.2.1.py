import re
import my_logger


class CriticalError(Exception):
    pass


def count_record(lines):
    records = 0
    record_pattern = re.compile('[0-9]{2}:[0-9]{2}:[0-9]{2}')
    for line in lines:
        if record_pattern.findall(line):
            records += 1
    return records


def count_errors(lines):
    errors = 0
    error_pattern = re.compile('.*Error.*|.*error.*|.*ERROR.*')
    critical_pattern = re.compile('.*CRITICAL ERROR.*')
    for line in lines:
        try:
            if critical_pattern.findall(line):
                raise CriticalError(line)
        except CriticalError:
            my_logger.logger.critical(line)
            errors += 1
        else:
            if error_pattern.findall(line):
                errors += 1
                my_logger.logger.error(line)
    return errors


def divide_lines_to_errors(record, error):
    try:
        division = record/error
    except ZeroDivisionError as e:
        return e
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
        return f'\n(количество записей в yupdate.log) / (количество записей с ошибками) = {divide_lines_to_errors(records, errors)}'


if __name__ == "__main__":
    print(read_file('yupdate.log'))

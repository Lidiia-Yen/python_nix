import logging
import re


def log_errors(myfile):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('found_errors.log')
    handler.setLevel(logging.ERROR)
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    logger.addHandler(handler)
    logger.addHandler(console)
    q_errors = 0
    lines = 0
    with open(myfile, 'r') as f:
        try:
            for line in f:
                lines += 1
                error = len(re.findall(r'ERROR|Error|error', line))
                q_errors += error
                critical = len(re.findall(r'CRITICAL|Critical|critical', line))
                if error != 0:
                    logger.error(line)
                    if critical != 0:
                        logger.critical(line)
                        try:
                            raise CriticalError(line)

                        except CriticalError as e:
                            print('It is a critical error ' + str(e))

        except ZeroDivisionError:
            print('You cannot divide by zero!')
        finally:
            k = lines / q_errors
            return k



class CriticalError(Exception):
    pass

if __name__ == "__main__":
    a = log_errors(myfile='yupdate.log')
    print(a)

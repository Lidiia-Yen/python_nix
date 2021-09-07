import logging
import re


def log_errors(myfile):  # в одной функции у тебя описана куча всего не связанного, как минимум логгер точно должен
    # быть либо отдельным классом, либо описан на уровне модуля. У функции должно быть 1 назначение, у тебя их тут 5
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('found_errors.log')
    handler.setLevel(logging.ERROR)
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    logger.addHandler(handler)
    logger.addHandler(console)
    q_errors = 0  # не понятное имя переменной
    lines = 0
    with open(myfile, 'r') as f:
        try:
            for line in f:
                lines += 1  # пересмотри структуру лога, такой алгоритм даст не верный результат
                error = len(re.findall(r'ERROR|Error|error', line))  # подумай, что ты здесь считаешь, и что нужно считать по заданию
                q_errors += error
                critical = len(re.findall(r'CRITICAL|Critical|critical', line))
                if error != 0:  # не очень хорошее решение привязываться к количеству для вывода лога, здесь лучше по результатам поиска
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



class CriticalError(Exception):  # используй автоформат, обращай внимание на замечания иде
    pass

if __name__ == "__main__":
    a = log_errors(myfile='yupdate.log')
    print(a)

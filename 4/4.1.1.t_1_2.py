import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler('logger_errors.log', 'w', 'utf-8')
logger.addHandler(fileHandler)


# task_1
def transliterate(function):
    def wrapper(text):
        result = ''
        letters_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
                        'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        for letter in text:
            result += (letters_dict.get(letter.lower(), letter.lower()).capitalize() if letter.isupper()
                       else letters_dict.get(letter, letter))
        return function(result)

    return wrapper


# task_2
def dec_trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"[time]: {datetime.datetime.now().strftime('%H:%M:%S')},[module]: {format(func.__module__)},["
                    f"function]: {format(func.__name__)},[arguments]: {args}, [return]: {result}\n")
        return result
    return wrapper


@dec_trace
@transliterate
def output_text(user_input):
    return user_input


if __name__ == '__main__':
    print(output_text('Яблоко упало. Щурясь, Юра долго смотрел на пол...'))

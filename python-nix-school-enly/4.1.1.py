import datetime

test = list(map(str, input()))


def dec_trace(arg, file_name='function_errors.log'):
    def outer(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(
                    f"[time]:{datetime.datetime.now().strftime('%H:%M:%S')},[module]:{format(func.__module__)},["
                    f"function]:{format(func.__name__)},[arguments]:{''.join(arg)}, [return]:{result}\n")

            return result

        return inner

    return outer


def decorate(function):
    def wrapper(word):
        result = []
        letters_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
                        'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

        for letter in word:
            if letter.isupper():
                result.append(letters_dict[letter.lower()].capitalize())
            elif letter.islower():
                result.append(letters_dict[letter.lower()])
            elif not letter.isalpha():
                result.append(letter)

        return function(result)

    return wrapper


@dec_trace(test)
@decorate
def print_func(arg):
    return ''.join(arg)


if __name__ == '__main__':  # разберись со значением этой конструкции, потому что структура модуля кривая
    print(print_func(test))

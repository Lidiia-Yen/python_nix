import datetime

test = input()


def dec_trace(arg, file_name='function_errors.log'):
    def outer(func):
        def inner(*args, **kwargs):
            resp = func(*args, **kwargs)
            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(
                    f'[time]:{datetime.datetime.now().strftime("%H:%M:%S")},[module]:{format(func.__module__)},['
                    f'function]:{format(func.__name__)},[arguments]:{arg}, [return]:{resp}\n')
                file.close()
            return resp

        return inner

    return outer


def decorate(function):
    def wrapper(word):  # плохое имя, тем более не лист
        result = []
        letters_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
                'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}  # плохое имя, не отражает сущности
        # + конфликт
        for i in word:
            if i in letters_dict: # ты могла бы избавиться от одного из стейтментов
                result.append(letters_dict[i])
            elif str(i).lower() in letters_dict:  # зачем здесь явное преобразование?
                result.append(str(letters_dict[str(i).lower()]).upper())  # зачем здесь явное преобразование?
                # + очень громоздкая конструкция
            else:
                result.append(i)
        return function(result)

    return wrapper



@dec_trace(test)
@decorate
def print_func(arg):
    return ''.join(list(arg))  # зачем преобразование? В пайтоне явные преобразования практически не нужны,
    # не делай их абы где


if __name__ == '__main__':  # разберись со значением этой конструкции, потому что структура модуля кривая
    print(print_func(test))  # работает не совсем корректно, попробуй транслитирировать "Щур"

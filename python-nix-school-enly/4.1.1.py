import datetime

test = input()

def dec_tras(arg, file_name='C:/Users/enly/function_errors.log'):  # автоформат + не рабочий скрипт
    def outer(func):
        def inner(*args, **kwargs):
            resp = func(*args, **kwargs)
            file = open(file_name, mode='a', encoding='utf-8')  # ты уже ранее использовала менеджер контекста,
            # почему не использовала его здесь?
            file_content = (
                    "[time]:" + str(datetime.datetime.now().strftime("%H:%M:%S")) +
                    " [module]: " + str(format(func.__module__)) +
                    " [function]: " + str(format(func.__name__)) +
                    " [arguments]: " + str(arg) +
                    " [return]: " + str(resp))  # почитай про f-стринги и почти всегда юзай их
            file.write(str(file_content) + '\n')  # почему не сделать это в предыдущей строке?
            file.close()
            return resp
        return inner
    return outer


def decorate(func):
    def wrapper(list):  # плохое имя, тем более не лист
        result = []
        dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
                'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}  # плохое имя, не отражает сущности
        # + конфликт
        for i in list:
            if i in dict:  # ты могла бы избавиться от одного из стейтментов
                result.append(dict[i])
            elif str(i).lower() in dict:  # зачем здесь явное преобразование?
                result.append(str(dict[str(i).lower()]).upper())  # зачем здесь явное преобразование?
                # + очень громоздкая конструкция
            else:
                result.append(i)
        return func(result)
    return wrapper


@dec_tras(test)
@decorate
def print_func(arg):
    return ''.join(list(arg))  # зачем преобразование? В пайтоне явные преобразования практически не нужны,
    # не делай их абы где


if __name__ == '__main__':  # разберись со значением этой конструкции, потому что структура модуля кривая
    print(print_func(test))  # работает не совсем корректно, попробуй транслитирировать "Щур"

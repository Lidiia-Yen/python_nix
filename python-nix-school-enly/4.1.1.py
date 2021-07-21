import datetime

test = input()

def dec_tras(arg, file_name='C:/Users/enly/function_errors.log'):
    def outer(func):
        def inner(*args, **kwargs):
            resp = func(*args, **kwargs)
            file = open(file_name, mode='a', encoding='utf-8')
            file_content = (
                    "[time]:" + str(datetime.datetime.now().strftime("%H:%M:%S")) +
                    " [module]: " + str(format(func.__module__)) +
                    " [function]: " + str(format(func.__name__)) +
                    " [arguments]: " + str(arg) +
                    " [return]: " + str(resp))
            file.write(str(file_content) + '\n')
            file.close()
            return resp
        return inner
    return outer


def decorate(func):
    def wrapper(list):
        result = []
        dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
                'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        for i in list:
            if i in dict:
                result.append(dict[i])
            elif str(i).lower() in dict:
                result.append(str(dict[str(i).lower()]).upper())
            else:
                result.append(i)
        return func(result)
    return wrapper


@dec_tras(test)
@decorate
def print_func(arg):
    return ''.join(list(arg))


if __name__ == '__main__':
    print(print_func(test))

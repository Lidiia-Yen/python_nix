def return_dif(file):
    lines_list = file.readlines()
    substring = "D:TUpdaterController::SetUniqueParam(429): eid:"
    eids = []

    for string in lines_list:
        if substring in string:
            eids.append(string)  # эти 4 строчки можно переписать в одну через list comprehension

    last_eid = eids[-1]  # лучше получить последние 2 строки одним объектом и преобразовывать их циклом, будет меньше
    # дублирования кода
    pre_last_eid = eids[-2]

    def string_to_dict(s):
        kv = s[57:].split(
            ';')  # что такое 57? так делать нельзя. А если поменяется чуть паттерн, будешь пересчитывать символы?
        dict = {}  # ide подчеркнула тебе имя переменной. Почитай, что она хочет. Такие имена могут привести к
        # непонятным косякам
        for i in kv:
            small = i.split('.')
            dict[small[0]] = small[1]
        return dict  # функция получилась громоздкой, преобразовать kv в словарь можно 1 строкой (или 2, если более правильно) через словарное включение

    dict_pre_last = string_to_dict(pre_last_eid)
    dict_last = string_to_dict(last_eid)

    general_dict = {}
    general_dict.update(dict_last)
    general_dict.update(dict_pre_last)

    dif_dict = {}
    for key, value in general_dict.items():
        if key not in dict_last or dict_last[key] != dict_pre_last[key]:
            dif_dict[key] = value
    return dif_dict  # в твоем ретурне не понятно, какие значения были в последней строке, какие в предпоследней


if __name__ == "__main__":
    log_file = open('yupdate-exec-yabrowser.log', 'r')
    print(return_dif(log_file))


def return_dif(file):
    lines_list = file.readlines()
    substring = "D:TUpdaterController::SetUniqueParam(429): eid:"
    eids = []

    for string in lines_list:
        if substring in string:
            eids.append(string)

    last_eid = eids[-1]
    pre_last_eid = eids[-2]

    def string_to_dict(s):
        kv = s[57:].split(';')
        dict = {}
        for i in kv:
            small = i.split('.')
            dict[small[0]] = small[1]
        return dict

    dict_pre_last = string_to_dict(pre_last_eid)
    dict_last = string_to_dict(last_eid)

    general_dict = {}
    general_dict.update(dict_last)
    general_dict.update(dict_pre_last)

    dif_dict = {}
    for key, value in general_dict.items():
        if key not in dict_last or dict_last[key] != dict_pre_last[key]:
            dif_dict[key] = value
    return dif_dict


if __name__ == "__main__":
    log_file = open('yupdate-exec-yabrowser.log', 'r')
    print(return_dif(log_file))

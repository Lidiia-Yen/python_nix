import re


def return_dif(file):
    lines_list = file.readlines()
    substring = "D:TUpdaterController::SetUniqueParam(429): eid:"

    eids = [string for string in lines_list if substring in string]
    needed_eids = eids[-2:]
    pre_last_eid, last_eid = needed_eids

    def string_to_dict(s):
        kv = re.findall(r'\w*\.\w*', s)
        kv_dict = {i.split('.')[0]: i.split('.')[1] for i in kv}
        return kv_dict

    dict_pre_last = string_to_dict(pre_last_eid)
    dict_last = string_to_dict(last_eid)

    values_in_last = {key: dict_last[key] for key in dict(set(dict_last.items()) - set(dict_pre_last.items()))}
    values_in_pre_last = {key: dict_pre_last[key] for key in dict(set(dict_pre_last.items()) - set(dict_last.items()))}
    general_dict_of_dif = {'values_in_last': values_in_last, 'values_in_pre_last': values_in_pre_last}
    return general_dict_of_dif


if __name__ == "__main__":
    log_file = open('yupdate-exec-yabrowser.log', 'r')
    print(return_dif(log_file))

111
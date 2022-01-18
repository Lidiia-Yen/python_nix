def find_line(all_lines):
    pattern_lines = [string.split("eid: ")[1] for string in all_lines if "eid: " in string]
    needed_lines = pattern_lines[-2:]
    return needed_lines


def decompose_line(all_lines):
    list_lines = []
    for line in find_line(all_lines):
        decomposed_lines = dict(params.split('.') for params in line.split(';'))
        list_lines.append(decomposed_lines)
    return list_lines


def compare_params(dict_pre_last, dict_last):
    difference_dict = {}
    for key in dict_last:
        if key in dict_pre_last:
            if dict_pre_last[key] != dict_last[key]:
                difference_dict[key] = {'pre_last': dict_pre_last[key], 'last': dict_last[key]}
        else:
            difference_dict[key] = {'pre_last': 'BLANK', 'last': dict_last[key]}

    for key in dict_pre_last:
        if key not in dict_last:
            difference_dict[key] = {'pre_last': dict_pre_last[key], 'last': 'BLANK'}

    return difference_dict


def return_result(all_lines):
    result = decompose_line(all_lines)
    return f'\nResult:{compare_params(result[0],result[1])}'


if __name__ == "__main__":
    with open('yupdate-exec-yabrowser.log', 'r') as log_file:
        lines = log_file.readlines()
    print(return_result(lines))


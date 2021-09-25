import re


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


def compare_params(dict1, dict2):
    difference_dict = {}
    for key in dict2:
        if key in dict1:
            if dict1[key] != dict2[key]:
                difference_dict[key] = {'last': dict1[key], 'second_to_last': dict2[key]}
        else:
            difference_dict[key] = {'last': 'BLANK', 'second_to_last': dict2[key]}

    for key in dict1:
        if key not in dict2 and key not in difference_dict:
            difference_dict[key] = {'last': dict1[key], 'second_to_last': 'BLANK'}

    return difference_dict


def return_result(all_lines):
    result = decompose_line(all_lines)
    return f'\nResult:{compare_params(result[0],result[1])}'


if __name__ == "__main__":
    with open('yupdate-exec-yabrowser.log', 'r') as log_file:
        lines = log_file.readlines()
    print(return_result(lines))

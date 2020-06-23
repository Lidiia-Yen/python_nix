import re


def log_parser(path):
    pattern = r'\w+\.\d+'
    ides = re.compile(pattern)

    filename = path
    with open(filename, "r") as logs:
        list_of_lines = logs.readlines()

    updates = []

    for line in list_of_lines[::-1]:
        if 'D:TUpdaterController::SetUniqueParam(429): eid:' in line:
            updates.append(line)
            if not len(updates) < 2:
                break

    params = []

    for last_update in updates:
        params.append(set(ides.findall(last_update)))
    print(params)

    diff = set.difference(*sorted(params, key=len, reverse=True))
    res = dict([x.split('.') for x in diff])
    print(res)
    return res


log_parser('log_file.txt')

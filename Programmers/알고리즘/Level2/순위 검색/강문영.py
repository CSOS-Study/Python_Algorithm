import re


def confirm_employee(info_list, require_info, score):
    cnt = 0

    for i in info_list:
        info_row = i.split()
        for info, require in zip(info_row[:4], require_info[:4]):
            if info not in require:
                if require == "-":
                    pass
                else:
                    break
        else:
            if int(info_row[-1]) >= int(score):
                cnt += 1

    return cnt


def solution(info, query):
    result = []

    for i in query:
        require_info = i.replace(" and", "").split()
        result.append(confirm_employee(info, require_info, require_info[-1]))
    return result
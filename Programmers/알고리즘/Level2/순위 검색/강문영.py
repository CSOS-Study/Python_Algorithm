# def confirm_employee(info_list, require_info, score):
#     cnt = 0
#
#     for i in info_list:
#         info_row = i.split()
#         for info, require in zip(info_row[:4], require_info[:4]):
#             if info not in require:
#                 if require == "-":
#                     pass
#                 else:
#                     break
#         else:
#             if int(info_row[-1]) >= int(score):
#                 cnt += 1
#
#     return cnt
#
#
# def solution(info, query):
#     result = []
#
#     for i in query:
#         require_info = i.replace(" and", "").split()
#         result.append(confirm_employee(info, require_info, require_info[-1]))
#     return result

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

result = []
employee_dict = defaultdict(list)


def extract_way_underbar():
    global result
    for i in range(1, 5):
        for way in combinations([0, 1, 2, 3], i):
            result.append(way)
    result.append(())


def extract_info(info_list):
    global result
    global employee_dict

    extract_way_underbar()
    for info_each in info_list:
        employee_split = info_each.split()
        for underbar_list in result:
            temp = list(employee_split)
            for change_underbar in underbar_list:
                temp[change_underbar] = "-"

            key = ''.join(temp[:4])
            if employee_dict.get(key):
                employee_dict[key].append(int(temp[-1]))
            else:
                employee_dict[key] = [int(temp[-1])]

    for val in employee_dict.values():
        val.sort()


def solution(info, query):
    global employee_dict
    extract_info(info)
    answer = []

    for i in query:
        require_info = i.replace(" and", "").split()
        score, require_info_str = int(require_info[-1]), ''.join(require_info[:4])

        if require_info_str in employee_dict:
            potential_employee_score = employee_dict[require_info_str]
            index = bisect_left(potential_employee_score, score)
            answer.append(len(potential_employee_score) - index)
        else:
            answer.append(0)
            continue

    return answer
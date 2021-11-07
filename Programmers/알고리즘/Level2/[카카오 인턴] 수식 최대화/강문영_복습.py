from itertools import permutations
import re

max_ = 0


# 항이 n개이면 연산자는 n-1개

def calculate_expression(cal_order, cal_list, num_list):
    global max_

    for cal_element in cal_order:
        idx = 0
        while idx < len(cal_list):
            if cal_list[idx] == cal_element:
                num_list[idx] = eval(str(num_list[idx]) + cal_list[idx] + str(num_list[idx + 1]))
                del num_list[idx + 1]
                del cal_list[idx]
            else:
                idx += 1
    max_ = max(max_, abs(int(num_list[0])))


def solution(expression):
    num_list = re.findall("[0-9]+", expression)
    cal_list = re.findall("[^0-9]+", expression)

    for cal_order in permutations(["+", "-", "*"], 3):
        calculate_expression(cal_order, list(cal_list), list(num_list))

    return max_
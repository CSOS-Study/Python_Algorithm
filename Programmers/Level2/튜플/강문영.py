import re


def solution(s):
    s = s[1:-1]
    s_list = re.findall("{[0-9+,?]+}", s)
    s_list.sort(key=lambda x: len(x))

    result = []

    for i in s_list:
        num_list = i[1:-1].split(",")
        for num in num_list:
            if num not in result:
                result.append(num)

    return list(map(int, result))
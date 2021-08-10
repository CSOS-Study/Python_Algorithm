import re

not_alpha_pattern = re.compile("[^a-z]")


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        if not not_alpha_pattern.search(temp):
            str1_list.append(temp)

    for j in range(len(str2) - 1):
        temp = str2[j] + str2[j + 1]
        if not not_alpha_pattern.search(temp):
            str2_list.append(temp)

    # 다중집합의 합집합
    str1_list_copy = str1_list.copy()
    str1_list_copy2 = str1_list.copy()

    for i in str2_list:
        if i not in str1_list_copy:
            str1_list_copy2.append(i)
        else:
            str1_list_copy.remove(i)

    # 다중집합의 교집합
    result = []
    for i in str2_list:
        if i in str1_list:
            str1_list.remove(i)
            result.append(i)

    similar_down = len(str1_list_copy2)
    similar_up = len(result)

    if similar_down == similar_up:
        return 65536

    return int((similar_up / similar_down) * 65536)
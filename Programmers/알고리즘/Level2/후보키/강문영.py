from itertools import combinations


def check_is_in(already_key, new_key):
    if len(list(filter(lambda x: x in already_key, new_key))) == len(already_key):
        return False
    return True


def extract_minimize_key(minimize_part, reverse_relation):
    cnt = 0
    result_compare = []

    for i in range(2, len(minimize_part) + 1):
        confirm_key_num = combinations(minimize_part, i)
        for key_pair in confirm_key_num:
            is_pass = True
            for key_pair_compare in result_compare:
                if not check_is_in(key_pair_compare, key_pair):
                    is_pass = False
                    break
            if not is_pass:
                continue
            target_key_list = list(zip(*(reverse_relation[num] for num in key_pair)))

            for key_list in target_key_list:
                if target_key_list.count(key_list) > 1:
                    break
            else:
                result_compare.append(key_pair)
                cnt += 1
    return cnt


# 내가 고려하지 못한점, 과목이랑 반은 후보키가 될 수 없다.


def solution(relation):
    cnt = 0
    minimize_part = []
    reverse_relation = list(zip(*relation))

    for idx, val in enumerate(reverse_relation):
        for element in val:
            if list(val).count(element) > 1:
                minimize_part.append(idx)
                break
        else:
            cnt += 1

    if len(minimize_part) < 2:
        return cnt
    else:
        return cnt + extract_minimize_key(minimize_part, reverse_relation)
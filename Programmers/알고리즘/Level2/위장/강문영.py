# from collections import defaultdict
#
#
# def solution(clothes):
#     clothes_dict = defaultdict(list)
#     for i in clothes:
#         clothes_dict[i[1]].append(i[0])
#
#     result = 0
#
#     if len(clothes_dict) > 1:
#         combinations_part = 1
#         for values in clothes_dict.values():
#             combinations_part *= len(values)
#             result += len(values)
#         result += combinations_part
#
#         return result
#
#     return len(clothes_dict[list(clothes_dict.keys())[0]])

## 이렇게 하면 여러개인데, 하나밖에 없는 것들에 대한 처리가 안된다.

# from collections import defaultdict
#
#
# def solution(clothes):
#     clothes_dict = defaultdict(list)
#     for i in clothes:
#         clothes_dict[i[1]].append(i[0])
#
#     result = 0
#     combinations_part = 1
#     for values in clothes_dict.values():
#         if len(values) > 1:
#             combinations_part *= len(values)
#         result += len(values)
#
#     if len(clothes_dict) == 1:
#         return result
#
#     return result + combinations_part

from collections import defaultdict
from itertools import combinations

#
# def solution(clothes):
#     clothes_dict = defaultdict(list)
#     for i in clothes:
#         clothes_dict[i[1]].append(i[0])
#
#     # n가지 의상 종류 중에서 뽑을 수 있는 종류의 가지 수
#     pick_cases = []
#     for pick_num in range(1, len(clothes_dict) + 1):
#         for case in combinations(list(clothes_dict.keys()), pick_num):
#             pick_cases.append(list(case))
#
#     result = 0
#     for wear_cases in pick_cases:
#         temp = 1
#         for wear in wear_cases:
#             temp *= len(clothes_dict[wear])
#         result += temp
#
#     return result

from itertools import combinations

def solution(clothes):
    answer = 1
    dic = dict()

    for cloth, Type in clothes:
        if(dic.get(Type) == None ):
            dic[Type] = [cloth]
            continue
        dic[Type].append(cloth)

    for Type in dic:
        answer *= len(dic[Type]) + 1

    return answer - 1
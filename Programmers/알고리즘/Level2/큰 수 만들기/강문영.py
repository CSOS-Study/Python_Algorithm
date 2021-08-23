# ## 순서대로 순서 뽑기 (for문으로 구현하기)
# from itertools import combinations
#
#
# def solution(number, k):
#     order_list = set()
#     for order in combinations(range(len(number)), k):
#         temp = tuple(sorted(order))
#         order_list.add(temp)
#
#     result = []
#
#     for pick_order in order_list:
#         temp = ""
#         for ord in range(len(number)):
#             if not ord in pick_order:
#                 temp += number[ord]
#         result.append(int(temp))
#
#     return str(max(result))

def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


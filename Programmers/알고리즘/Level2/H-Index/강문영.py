# def solution(citations):
#     citations.sort()
#     result = []
#
#     for i in citations:
#         if len(list(filter(lambda x: x >= i, citations))) == i:
#             if len(list(filter(lambda x: x <= i, citations))) == len(citations) - i + 1:
#                 result.append(i)
#
#     if len(result) > 0:
#         return max(result)
#     else:
#         return 0


def solution(citations):
    citations.sort()

    for i in range(citations[-1], 1, -1):
        if len(list(filter(lambda x: x >= i, citations))) >= i:
            if len(list(filter(lambda x: x <= i, citations))) <= i:
                return i
    else:
        return 0
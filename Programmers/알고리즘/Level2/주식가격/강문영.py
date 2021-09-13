from collections import deque


# def solution(prices):
#     price_arr = []
#
#     for idx, price in enumerate(prices):
#         cnt = 0
#         if idx < len(prices) - 1:
#             for cpr_price in prices[idx + 1:]:
#                 cnt += 1
#                 if price > cpr_price:
#                     break
#
#         price_arr.append(cnt)
#
#     return price_arr


# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
def solution(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)]

    stack = [0]
    for i in range(1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
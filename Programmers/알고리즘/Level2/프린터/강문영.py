# from collections import deque
#
# def solution(priorities, location):
#     idx = -1
#     cnt = 0
#     n = len(priorities)
#     while True:
#         temp = priorities.pop(0)
#         idx += 1
#
#         if len(list(filter(lambda x: x > temp, priorities))) > 0:
#             priorities.append(temp)
#
#         else:
#             cnt += 1
#             if idx % n == location:
#                 return cnt


from collections import deque


def solution(priorities, location):
    d = deque([(v, i) for i, v in enumerate(priorities)])
    cnt = 0

    while True:
        temp = d.popleft()

        if len(list(filter(lambda x: x[0] > temp[0], d))) > 0:
            d.append(temp)
        else:
            cnt += 1
            if temp[1] == location:
                return cnt
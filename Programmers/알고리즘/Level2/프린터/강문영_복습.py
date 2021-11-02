from collections import deque


def solution(priorities, location):
    cnt = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while True:
        temp = d.popleft()

        if len(list(filter(lambda x: x[0] > temp[0], d))) > 0:
            d.append(temp)
        else:
            cnt += 1
            if temp[1] == location:
                return cnt
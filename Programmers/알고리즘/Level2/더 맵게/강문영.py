# def solution(scoville, K):
#     cnt = 0
#     num = len(scoville)
#
#     while True:
#         if list(filter(lambda x: x >= K, scoville)) == scoville:
#             break
#         scoville.sort()
#         scoville.append(scoville.pop(0) + scoville.pop(0) * 2)
#         cnt += 1
#     return cnt
# 이렇게 하면 모든 원소를 K로 만들 수 없을때 런타임 에러나, 시간초과가 난다.
# 그리고 sort를 계속 반복하는건 정답이 되기는 좀 힘들다. => sort가 계속 반복된다면 힙을 생각해보자
# sort가 반복되면 최대값을 구하거나, 최소값을 구하는데 이 경우 자체가 이미 힙에 구현이 되어있다.


import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            return cnt
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        temp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, temp)

        cnt += 1
    return cnt






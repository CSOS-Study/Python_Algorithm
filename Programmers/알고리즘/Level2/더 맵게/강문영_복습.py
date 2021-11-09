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
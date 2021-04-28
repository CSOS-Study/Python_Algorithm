'''
이전에 k광년 이동 -> 다음번 작동시 k-1, k, k+1 중 하나의 광년만큼 이동 가능
y행성에 도착하기 바로 직전 이동거리는 1광년이어야 함
x에서 y까지 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하라

1. (N의 제곱)일 때까지는 2 * N - 1
2. (N의 제곱 + N)이하일 때까지는 2 * N 횟수를 가짐.
'''
import math
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y-x
    if dist == 1 or dist ==2:
        print(dist)
    else:
        N = int(math.sqrt(dist))
        if dist == N **2: print(2*N-1)
        elif N < dist <= N**2 + N : print(2*N)
        else: print((N+1)*2 -1)
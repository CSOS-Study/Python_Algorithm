import sys

N = int(input())
list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
list.sort()
for i in list:
    print(i[0], i[1])
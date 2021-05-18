import sys

case=[sys.stdin.readline().strip().split(' ') for _ in range(int(input()))]
for i,j in sorted(case, key=lambda x:int(x[0])):
    print(i,j)
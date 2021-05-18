import sys

N = int(input())
members = [sys.stdin.readline().rstrip().split() for _ in range(N)]
members.sort(key=lambda m:int(m[0]))

for m in members:
    print(' '.join(m))

#파이썬 sort함수는 정렬할때 순서를 유지한다.
import collections
import sys

dic = collections.defaultdict(int)
N = int(sys.stdin.readline())
for _ in range(N):
    dic[int(sys.stdin.readline())] += 1

res = sorted(dic.items())
for num, cnt in res:
    for _ in range(cnt):
        print(num)
#dict정렬
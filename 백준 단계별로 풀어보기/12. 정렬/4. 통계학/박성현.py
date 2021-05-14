import sys
from collections import Counter

n=int(sys.stdin.readline())
case=sorted([int(sys.stdin.readline()) for _ in range(n)])
print(round(sum(case)/n))
print(case[(n-1)//2])
cnt_case=Counter(case).most_common()
print(cnt_case[0][0] if len(cnt_case)==1 or cnt_case[0][1]>cnt_case[1][1] else cnt_case[1][0])
print(max(case)-min(case))
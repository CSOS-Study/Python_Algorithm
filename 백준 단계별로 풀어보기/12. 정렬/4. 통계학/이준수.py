import sys
import collections

N = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(N)]
list.sort()

print(round(sum(list)/N))
print(list[N//2])

print(collections.Counter(list))
lmc = collections.Counter(list).most_common(2)
frequency = lmc[-1][0] if lmc[0][1] == lmc[-1][1] else lmc[0][0]

print(frequency)
print(max(list) - min(list))

#삼항연산자
#파이썬 반올림 round(실수,n)
#list의 인덱스 순번대로(처음나오는값) collections.Counter(list)은 반환한다.
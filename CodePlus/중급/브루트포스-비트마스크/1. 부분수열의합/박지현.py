'''
range(1<<n) : 수열이 n개 있을 때 가능한 부분수열의 개수
n = 2 이면 가능한 부분수열 3개 (1<<2) # 4-1 range니까
n = 3 이면 가능한 부분수열 7개 (1<<3)

i & 1 << j 부분 : 모든 부분수열의 합을 구하는 과정
i =1일 때,
j=0이면 -> 1
j=1이면 -> 0
j=2이면 -> 0
=> s[0]를 더한다.

i =2일 때,
j=0이면 -> 0
j=1이면 -> 1
j=2이면 -> 0
=> s[1]을 더한다.

i =3일 때,
j=0이면 -> 1
j=1이면 -> 1
j=2이면 -> 0
=> s[0]+s[1]을 더한다.
'''
n = int(input())
s = list(map(int,input().split()))
check = set(range(1,20*100000))

for i in range(1<<n): # 0~7을 순회
    total = 0
    for j in range(n):
        if i & 1 << j:
            total+=s[j]
    check.discard(total)

print(min(check))



'''
# combinations으로 푼 경우

from itertools import combinations
import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))
check = [False] * (sum(s)+2)

for i in range(1,n+1):
    for j in combinations(s,i):
        check[sum(j)] = True

print(check[1:].index(False)+1)
'''

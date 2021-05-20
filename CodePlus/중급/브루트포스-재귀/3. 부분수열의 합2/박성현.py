from itertools import combinations

N = int(input())
case = list(map(int, input().split()))
chk = [0] * (sum(case)+1)
for i in range(1, N+1):
    for j in combinations(case, i):
        chk[sum(j)] = 1
print(chk[1:].index(0)+1 if 0 in chk[1:] else sum(case)+1)
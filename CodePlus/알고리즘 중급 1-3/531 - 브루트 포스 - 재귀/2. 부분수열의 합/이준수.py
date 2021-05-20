from itertools import combinations

N, S = map(int, input().split())
l = list(map(int, input().split()))

res = 0
for i in range(1, N+1):
    res += len(list(filter(lambda x: sum(x) == S, combinations(l,i))))

print(res)
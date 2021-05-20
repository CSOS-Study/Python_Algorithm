from itertools import combinations
n,s = map(int,input().split())
n_list = list(map(int,input().split()))

result = 0
for i in range(1,n+1):
    for j in combinations(n_list,i):
        if sum(j) == s:
            result +=1

print(result)
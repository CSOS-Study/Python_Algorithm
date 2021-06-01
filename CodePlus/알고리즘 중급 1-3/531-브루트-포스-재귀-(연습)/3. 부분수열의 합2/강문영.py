from itertools import combinations

n = int(input())
n_list = list(map(int,input().split()))

check_list = [0]*(sum(n_list)+2)
check_list[0] = 1


check_list = [1] + [0]*[n+1]

for i in range(1,n+1):
    for j in combinations(n_list,i):
        check_list[sum(j)]=1

print(check_list.index(0))
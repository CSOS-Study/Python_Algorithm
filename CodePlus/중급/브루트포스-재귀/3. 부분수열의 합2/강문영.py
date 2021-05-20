from itertools import combinations

n = int(input())
n_list = list(map(int,input().split()))

check_list = [0]*100000000

for i in range(1,n+1):
    for j in combinations(n_list,i):
        check_list[sum(j)]=1

for idx,val in enumerate(check_list):
    if val == 0 and idx>0:
        print(idx)
        break
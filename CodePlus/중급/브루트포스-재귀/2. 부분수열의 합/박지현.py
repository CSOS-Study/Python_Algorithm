from itertools import combinations

def search(n_lst,val):
    if val > n:
        print(len(p))
        return
    for i in combinations(n_lst,val):
        if sum(i) == s: p.append(i)
    search(n_lst,val+1)

n, s = map(int,input().split())
n_lst = list(map(int, input().split()))
p=[]
search(n_lst,1)
from itertools import combinations

def sol(s,i):
    if i > len(s): return
    for a in combinations(s,i):
        check[sum(a)] = True
    sol(s,i+1)

n = int(input())
s = list(map(int,input().split()))
check = [False]*(sum(s)+2) #s의 모든 경우로 수열 생성이 가능하다면, 그 다음 첫번째 자연수를 출력해야함.
sol(s,1)
print(check[1:].index(False)+1)
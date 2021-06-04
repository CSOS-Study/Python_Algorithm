from itertools import permutations

def sol(i):
    for j in range(k):
        if op[j] == '<' and i[j] > i[j+1]: return False
        elif op[j] == '>' and i[j] < i[j+1]: return False
    return True

k = int(input())
op = list(input().split())

for i in permutations([9,8,7,6,5,4,3,2,1,0],k+1):
    if sol(i):
        print(''.join(list(map(str,i))))
        break
for i in permutations([0,1,2,3,4,5,6,7,8,9],k+1):
    if sol(i):
        print(''.join(list(map(str,i))))
        break
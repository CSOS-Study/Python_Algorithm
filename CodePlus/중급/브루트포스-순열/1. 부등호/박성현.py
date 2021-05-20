from itertools import permutations
import sys

def sol(perm):
    for i in perm:
        chk=True
        for j in range(k):
            if A[j] == '<' and i[j] >= i[j + 1]:
                chk&=False
                break
            if A[j] == '>' and i[j] <= i[j + 1]:
                chk&=False
                break
        if chk:
            return print(''.join(list(map(str, i))))

print(permutations([0,1,2,3,4,5,6,7,8,9], 6+1))
k=int(sys.stdin.readline())
A=sys.stdin.readline().split()
perm=list(permutations([0,1,2,3,4,5,6,7,8,9], k+1))
sol(reversed(perm))
sol(perm)
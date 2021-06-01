import sys
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
opers = ''.join(['+', '-', '*', '/'][idx] * i
               for idx, i in enumerate(map(int, input().split())))

min_res = sys.maxsize
max_res = -sys.maxsize

#set중요.
for oper in set(permutations(opers, N-1)):
    res = A[0]
    for i in range(0, N-1):
        if oper[i] == '+':
            res += A[i+1]
        elif oper[i] == '-':
            res -= A[i+1]
        elif oper[i] == '*':
            res *= A[i+1]
        else:
            if res < 0:
                res = -(-res // A[i+1])
            else:
                res //= A[i+1]
            #int(res/A[+1])와 같다.
    min_res = min(res, min_res)
    max_res = max(res, max_res)

print(max_res)
print(min_res)

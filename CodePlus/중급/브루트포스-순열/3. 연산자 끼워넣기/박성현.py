from itertools import permutations

n=int(input())
case=list(map(int, input().split()))
op=['+', '-', 'x', '//']

opcase=[]
for i,j in zip(op, list(map(int, input().split()))):
    opcase.extend([i]*j)

def oper(l, r, m):
    if m=='+':
        return l+r
    elif m=='-':
        return l-r
    elif m=='x':
        return l*r
    else:
        return int(l/r)


def sol():
    global res
    for i in permutations(opcase, n-1):
        tmp=case[0]
        for j in range(len(i)):
            tmp=oper(tmp,case[j+1],i[j])
        res.append(tmp)

res=[]
sol()
print(max(res), min(res),sep='\n')
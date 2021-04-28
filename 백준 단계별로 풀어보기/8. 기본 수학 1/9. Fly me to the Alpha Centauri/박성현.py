import math

n = int(input())
g = [map(int, input().split()) for _ in range(n)]
for i, j in g:
    dis = j - i
    sq = int(math.sqrt(dis))
    if sq == 1:
        print(dis)
    elif dis >= sq*(sq+1)+1:
        print(sq*2 + 1)
    elif dis >= sq**2 + 1:
        print(sq * 2)
    else:
        print(sq*2 - 1)

# 틀린 답안
''' 
n = int(input())
g = [map(int, input().split()) for _ in range(n)]
for a, b in g:
    cnt = 0
    goal = [b-1, b+1]
    d = {a:set([1])}
    while a != -1:
        for i in d[a]:
            d.setdefault(a+i, set())
            for j in (i-1, i, i+1):
                if j>0:
                    d[a+i].add(j)
        a += 1
        cnt += 1
        for i, j in zip(goal, [1, -1]):
            if i in d.keys() and j in d[i]:
                print(cnt+1)
                a = -1
'''
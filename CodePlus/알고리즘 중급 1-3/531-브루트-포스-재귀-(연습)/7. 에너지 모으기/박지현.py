import sys

def sol(total,w):
    global mx
    if len(w) == 2:
        mx = max(mx,total)
        return
    for i in range(1,len(w)-1):
        t = w[i - 1] * w[i + 1]
        temp = w[i]
        del w[i]
        sol(total+t,w)
        w.insert(i,temp)

N = int(input())
w = list(map(int,sys.stdin.readline().split()))
mx = 0

sol(0,w)
print(mx)
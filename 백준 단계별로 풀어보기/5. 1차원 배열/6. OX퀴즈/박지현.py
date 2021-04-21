import sys
N=int(input())
for i in range(N):
    lst = list(sys.stdin.readline())
    cnt=0
    total=0
    for i in range(len(lst)):
        cnt= cnt+1 if lst[i]=='O' else 0
        total+=cnt
    print(total)
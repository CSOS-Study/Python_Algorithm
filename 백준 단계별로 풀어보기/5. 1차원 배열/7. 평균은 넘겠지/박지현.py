import sys
C=int(input())

for i in range(C):
    cnt=0
    N=list(map(int,sys.stdin.readline().split()))
    avg=sum(N[1:])/N[0]
    for i in N[1:]:
        if i>avg:
            cnt += 1
    ratio=cnt/N[0]*100
    print(format(ratio,".3f")+"%")
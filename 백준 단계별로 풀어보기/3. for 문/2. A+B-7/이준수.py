import sys
N=int(input())

for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #%d:"%(i+1),a+b)
import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
max=max(A)
for i in range(N):
    A[i]=A[i]/max*100
print(sum(A)/N)
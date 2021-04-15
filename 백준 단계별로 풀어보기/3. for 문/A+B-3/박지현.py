N=int(input())
lst=[]
for i in range(N):
    A,B=map(int, input().split())
    lst.append(A+B)
for i in range(N):
    print(lst[i])
n,x = map(int,input().split())
n_list = list(map(int,input().split()))

min = x
for i in n_list:
    temp = i
    if(i<min):
        print(i,end=" ")


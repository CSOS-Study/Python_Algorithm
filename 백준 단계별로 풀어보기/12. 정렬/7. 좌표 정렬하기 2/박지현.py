import sys
xy_lst=[]

for _ in range(int(sys.stdin.readline())):
    xy = list(map(int, sys.stdin.readline().split()))
    xy_lst.append(xy)
xy_lst.sort(key=lambda x:(x[1],x[0])) #1인덱스 정렬 -> 0인덱스 정렬

for i in range(len(xy_lst)):
    print(xy_lst[i][0],xy_lst[i][1], sep=' ')
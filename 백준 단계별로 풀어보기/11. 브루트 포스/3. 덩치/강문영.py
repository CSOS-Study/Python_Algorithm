n = int(input())
n_list = []
for i in range(n):
    n_list.append(tuple(map(int,input().split())))

for i in range(n):
    cnt = 1
    for j in range(n):
        if n_list[i][0]<n_list[j][0] and n_list[i][1]<n_list[j][1]:
            cnt +=1
    print(cnt,end=' ')





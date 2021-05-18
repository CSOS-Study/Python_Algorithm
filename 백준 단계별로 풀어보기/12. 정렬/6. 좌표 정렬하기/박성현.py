case=[list(map(int, input().split())) for _ in range(int(input()))]
for i,j in sorted(case, key=lambda x:(x[0],x[1])):
    print(i,j)
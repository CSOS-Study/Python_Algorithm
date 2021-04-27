C = int(input())
for _ in range(C):
    l = list(map(int,input().split()))
    avg = sum(l[1:]) / l[0]
    cnt = 0
    for i in l[1:]:
        if(i > avg):
            cnt+=1
    percentage = cnt/l[0]*100
    print("{0:0.3f}%".format(percentage))

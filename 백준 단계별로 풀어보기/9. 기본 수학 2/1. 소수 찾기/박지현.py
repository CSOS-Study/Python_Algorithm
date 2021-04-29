N, total = int(input()), 0
num_lst = list(map(int,input().split()))
for num in num_lst:
    if num==1:continue
    cnt=1
    for i in range(2,num):
        if num % i == 0: cnt += 1 #break 넣는게 좋음(시간초과 대비)
    if cnt==1: total+=1
print(total)
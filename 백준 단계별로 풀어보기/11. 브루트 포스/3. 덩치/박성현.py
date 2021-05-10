n=int(input())
case = [list(map(int, input().split())) for _ in range(n)]
res=''
for i in range(n):
    w, h = case.pop(i)
    cnt=0
    for dw, dh in case:
        if w<dw and h<dh:
            cnt+=1
    res+=str(cnt+1)+' '
    case.insert(i,[w,h])
print(res.rstrip())
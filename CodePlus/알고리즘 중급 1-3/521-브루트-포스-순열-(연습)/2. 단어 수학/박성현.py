from collections import defaultdict

n=int(input())
f=[[i for i in str(input())[::-1]] for _ in range(n)]
d=defaultdict(int)
for f_ in f:
    c=1
    for i in f_:
        d[i]+=c
        c*=10
s=9
ans=0
for _,i in sorted(d.items(),key=lambda x:x[1],reverse=True):
    ans+=i*s
    s-=1
print(ans)


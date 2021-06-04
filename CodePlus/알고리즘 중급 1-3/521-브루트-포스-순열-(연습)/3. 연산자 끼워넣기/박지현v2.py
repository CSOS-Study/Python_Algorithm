t=int(input())
s=list(map(int,input().split()))
op=list(map(int,input().split()))
mx,mn=-10000000000,10000000000

def sol(total,i,add,sub,mul,div):
    global mx, mn
    if i==t-1:
        mx=max(mx,total)
        mn=min(mn,total)
        return

    if add >0:
        sol(total+s[i+1],i+1,add-1,sub,mul,div)
    if sub >0:
        sol(total-s[i+1],i+1,add,sub-1,mul,div)
    if mul >0:
        sol(total*s[i+1],i+1,add,sub,mul-1,div)
    if div >0:
        sol(int(total/s[i+1]),i+1,add,sub,mul,div-1)

sol(s[0],0,op[0],op[1],op[2],op[3])
print(mx,mn,sep='\n')
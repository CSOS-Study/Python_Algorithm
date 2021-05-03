def sol(a=0, b=1, cnt=1):
    tmp = a+b
    a = b
    b = tmp
    cnt += 1
    if n==cnt:
        return print(tmp)
    elif n==0 or n==1:
        return print(n)
    sol(a, b, cnt)
    
n = int(input())
sol()
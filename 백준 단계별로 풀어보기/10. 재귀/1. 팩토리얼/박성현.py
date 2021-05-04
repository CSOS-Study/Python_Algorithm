def sol(n, res=1):
    if n==1 or not n: 
        print(res)
        return
    res *= n
    n -= 1
    sol(n, res)

sol(int(input()))
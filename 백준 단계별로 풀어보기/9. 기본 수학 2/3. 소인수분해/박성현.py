def sol(n):
    for i in range(2, n+1):
        if not n%i:
            print(i)
            sol(n//i)
            break

n = int(input())
sol(n)
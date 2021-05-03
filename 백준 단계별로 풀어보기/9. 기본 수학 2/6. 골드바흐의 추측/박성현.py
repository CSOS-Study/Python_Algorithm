def sol(num):
    if num==1: return False
    for i in range(2, int(num**0.5)+1):
        if not num%i:
            return False
    return True

case = [int(input()) for _ in range(int(input()))]
max_c = max(case) + 1
prime = [False] * max_c
for i in range(2, max_c-1):
    prime[i] = sol(i)
for i in case:
    div = i//2
    while True:
        if prime[div] and prime[i-div]:
            print(div, i-div)
            break
        div-=1
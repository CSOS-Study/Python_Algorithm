def sol(num):
    if num==1: return False
    for i in range(2, int(num**0.5)+1):
        if not num%i:
            return False
    return True

n = 123456*2 + 1
case = [False] * n
for i in range(2, 123456*2):
    case[i] = sol(i)
    
while True:
    n, cnt = int(input()), 0
    if n==0: break
    for i in case[n+1:2*n+1]:
        if i: cnt+=1
    print(cnt)
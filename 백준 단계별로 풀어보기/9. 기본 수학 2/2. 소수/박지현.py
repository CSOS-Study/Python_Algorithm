M,N,prime_lst = int(input()), int(input()), []
for i in range(M,N+1):
    if i == 1: continue
    cnt = 1
    for num in range(2, i):
        if i % num == 0:
            cnt += 1
            break #소수아닌거 판별났으니까 뒤로는 더 검사 안해도됨
    if cnt==1: prime_lst.append(i)

if len(prime_lst)<1: print(-1)
else: print(sum(prime_lst),prime_lst[0], sep='\n')
N = int(input())
prime_lst=[]
if N ==1: exit()
while True:
    if N == 1: break #소수로 나뉘어져서 1이 된 경우 끝내기
    for i in range(2,N+1): #N이 소수면 소인수:N
        if N % i == 0:
            prime_lst.append(i)
            N = N // i
            break
prime_lst.sort()
for i in prime_lst: print(i)
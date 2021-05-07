import math

def prime(num):
    if num == 1: return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0: return False # num이 i의 배수라면 return false, 함수 종료
        else : pass
    return True

pre_lst = [True] * (123456*2+1)
for i in range(2,123456 * 2):
    pre_lst[i]=prime(i)

while True:
    n,cnt = int(input()), 0
    if n == 0: exit()
    for i in pre_lst[n+1:2*n+1]: #소수만 미리 뽑아둔거에서 탐색만
        if i: cnt+=1 #이 범위만큼 prime()검사를 매번 하고 있음 -> 비효율적
    print(cnt)

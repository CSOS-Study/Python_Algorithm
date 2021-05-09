'''
골드바흐 파티션:
2보다 큰 짝수 N은 두 소수의 합으로 계산할 수 있으며,
이때 이 두 소스를 골드바흐 파티션이라고 한다.

N을 입력받고, N보다 작은 소수 List를 생성하고,
for문 돌려서 N-소수==0인거 찾고,
만약 두 소수의 차가 이전거보다 크다면 PASS 아니면 갱신
'''
def prime(num):
    if num == 1: return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0: return False # num이 i의 배수라면 return false, 함수 종료
        else : pass
    return True

prime_lst= [False] * 10001
for i in range(2,len(prime_lst)):
    prime_lst[i]=prime(i)

for _ in range(int(input())):
    n = int(input())
    half_1 = n//2
    half_2 = half_1
    while True:
        if prime_lst[half_1] and prime_lst[half_2]:
            print(half_2,half_1)
            break
        half_1+=1
        half_2-=1

'''
특정 범위에서 소수 찾기 : 에라토스테네스의 체 알고리즘 활용

- 전체 범위에서 소수(2,3,5...)의 배수를 없앤다.
- 범위가 120까지라면 120의 제곱근 (~= 11) 안쪽 소수의 배수만 삭제하면 됨
'''
import math

def prime(num):
    if num == 1: return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0: return False # num이 i의 배수라면 return false, 함수 종료
        else : pass
    return True

M,N = map(int,input().split())
for i in range(M,N+1):
    if prime(i) : print(i)
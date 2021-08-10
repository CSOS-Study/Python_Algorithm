from itertools import combinations

def is_decimal(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def solution(nums):
    result = 0
    for i in combinations(nums,3):
        if(is_decimal(sum(i))):
            result +=1

    return result
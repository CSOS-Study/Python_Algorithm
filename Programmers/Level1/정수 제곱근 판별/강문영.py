import math
def solution(n):
    sqrt_num = int(math.sqrt(n))
    if sqrt_num**2 == n:
        return (sqrt_num+1)**2
    return -1
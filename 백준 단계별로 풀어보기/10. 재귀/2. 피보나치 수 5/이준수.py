'''
from functools import lru_cache
@lru_cache(None)
==> memoization을 자동으로 해준다고 함.

재귀는 base case가 가장 중요한 포인트임.
모든 함수가 base case로 끝날수있는지 검증해야함.
'''
from functools import lru_cache


@lru_cache(None)
def fibonacci(n:int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(int(input())))
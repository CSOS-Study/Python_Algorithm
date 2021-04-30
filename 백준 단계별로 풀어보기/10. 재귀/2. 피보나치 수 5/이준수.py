from functools import lru_cache
@lru_cache(None)
def fibonacci(n:int) -> int:
    if(n <= 0): return 0
    if(n == 1): return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))
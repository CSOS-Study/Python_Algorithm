def fibonacci(n):
    if n<= 1 : return n
    else: return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))


'''
0, 1
0, 1, 0+1
0, 1, 0+1, 1+1,
0, 1, 0+1, 1+1, 1+2
0, 1, 0+1, 1+1, 1+2, 2+3
0, 1, 0+1, 1+1, 1+2, 2+3, 3+5

1) n=3 일때, return fibonacci(2) + fibonacci(1)
2) n=2 일때, return fibonacci(1) + fibonacci(0)
3) 즉, 다 조합해보면 fibonacci(1) + fibonacci(0) + fibonacci(1)
'''

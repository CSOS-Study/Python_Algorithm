'''
N! 구하는 문제,
ex) 3! = 3 * 2 * 1
'''
def factorial(n):
    if n == 0 or n == 1 : return 1
    else: return n * factorial(n-1)

N = int(input())
print(factorial(N))
'''
1) 3 입력 : return 3 * factorial(2)
2) 2 입력 : return 2 * factorial(1)
3) 1 입력 : return 1
=> 처음 3 입력했을 때 1) 3 * factorial(2)였던거에 대입하면,
   3 * 2 * 1 이 최종 return 된다.
'''
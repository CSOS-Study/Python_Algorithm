'''
주의해야할것 : 0! = 1
함수의 정의 : 1부터 n까지의 곱을 반환한다.
함수는 다음과 같이 쪼갤수있다.
n * 1부터 n-1까지의 곱
==> n * factorial(n-1)
'''
def factorial(n:int) -> int:
    if(n<=1):
        return 1
    return n * factorial(n-1)


print(factorial(int(input())))


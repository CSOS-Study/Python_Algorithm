'''
어떤수를 두개의 수의 합으로 쪼겠을때, 두개의 수의 차이가 가장 작을때는 절반으로 쪼겠을때 가장 작다.
절반에서 멀어질수록 한쪽은 증가하고 한쪽은 감소하므로 그 차이는 더 커진다.
'''

prime = [True] * (10000 + 1)  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 10000 + 1):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 10000 + 1, n):
                prime[m] = False


sieve()
T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2, -1, -1):
        j = n - i
        if prime[i] and prime[j]:
            print(i,j)
            break
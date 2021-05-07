prime = [True] * (123456 * 2 + 1)  # 소수이면 True


def sieve():
    prime[1] = False
    for n in range(2, 123456 * 2 + 1):
        if prime[n]:  # n 가 소수인경우
            for m in range(n + n, 123456 * 2 + 1, n):
                prime[m] = False


sieve()
while True:
    n = int(input())
    if not n:
        break
    print(prime[n+1:2*n+1].count(True))
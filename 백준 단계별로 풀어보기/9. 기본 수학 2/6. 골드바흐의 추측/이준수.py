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
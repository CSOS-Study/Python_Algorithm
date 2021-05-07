n = int(input())
n_list = list(map(int, input().split()))

def is_prime(n):
    if n<2:
        return 0
    for j in range(2, n):
        if n % j == 0:
            return 0
    return 1

result =0
for i in n_list:
    result += is_prime(i)

print(result)

## 에라토스테네스의 체
## 루프 돌려서 하나씩 검증

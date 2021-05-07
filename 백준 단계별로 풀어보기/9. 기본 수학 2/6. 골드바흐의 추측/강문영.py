n = int(input())

prime = [True] * 10001  # 소수이면 True
prime[1] = False
for n in range(2, 10001):
    if prime[n]:  # n 가 소수인경우
        for m in range(n + n, 10001, n):
            prime[m] = False

for _ in range(n):
    target_number = int(input())
    res_list = [i for i, value in enumerate(prime) if value == True and (i >= 2 and i <= target_number)]
    min = 1111
    result = 0
    for j in res_list:
        if (target_number - j) in res_list:
            if abs(2*j - target_number)< min:
                min = abs(2*j - target_number)
                result = j

    print(result,target_number-result)



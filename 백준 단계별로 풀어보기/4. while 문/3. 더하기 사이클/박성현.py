# 3번
cnt = 0
n = sn = int(input())
while True:
    cnt += 1
    n = (n % 10) * 10 + (n // 10 + n % 10) % 10
    if sn == n:
        print(cnt)
        break
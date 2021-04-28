n, r, cnt = int(input()), 1, 1
while n > (6 * cnt + r):
    r += 6 * cnt
    cnt += 1
print(cnt + 1 if n > 1 else 1)

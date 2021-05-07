n, cnt, s = int(input()), 1, 1
while True:
    if s <= n < s + cnt or n == 1:
        break
    s += cnt
    cnt += 1
r = range(1, cnt + 1)
chk = n - s + 1
if cnt % 2 != 0:
    print('{}/{}'.format(r[cnt - chk], r[chk - 1]))
else:
    print('{}/{}'.format(r[chk-1], r[cnt - chk]))

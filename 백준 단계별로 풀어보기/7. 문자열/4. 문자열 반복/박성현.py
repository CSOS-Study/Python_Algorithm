n, ans = int(input()), ''
for _ in range(n):
    a, b = map(str, input().split())
    for i in b:
        ans += i * int(a)
    ans += '\n'
print(ans)

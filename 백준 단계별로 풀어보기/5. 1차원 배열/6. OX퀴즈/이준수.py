n = int(input())
for i in range(n):
    s = input()
    ans = 0
    _ = 0
    for c in s:
        if(c=='O'):
            _ += 1
        else:
            _ = 0
        ans += _
    print(ans)
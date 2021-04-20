n = int(input())
l, ans = [str(input()) for _ in range(n)], [0] * n
for i in range(n):
    cnt = 0
    for j in l[i]:
        if j == 'O':
            cnt += 1
            ans[i] += cnt
        else:
            cnt = 0
for i in ans: print(i)

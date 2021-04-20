n = int(input())
ans = []
for _ in range(n):
    l, cnt = list(map(int, input().split())), 0
    tn = l[0]
    avg = sum(l[1:]) / tn
    for i in l[1:]:
        if i > avg: cnt += 1
    ans.append(cnt / tn * 100)
for i in ans: print("{:.3f}%".format(i))
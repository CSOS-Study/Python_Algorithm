N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

res = 0

for i in range(N-2):
    l,r = i+1, N-1
    while l < r:
        s = card[i] + card[l] + card[r]
        if s <= M:
            res = max(res,s)
            l += 1
        else:
            r -= 1
print(res)
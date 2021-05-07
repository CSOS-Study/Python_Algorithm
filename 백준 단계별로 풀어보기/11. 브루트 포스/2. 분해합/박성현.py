n, res = int(input()), 0
for i in range(1, n+1):
    cost = i+sum([int(j) for j in str(i)])
    if cost==n:
        res = i
        break
print(res if res else 0)
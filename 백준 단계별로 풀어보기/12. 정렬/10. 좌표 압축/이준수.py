N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(set(X))

map = {}
for idx, num in enumerate(sorted_X):
    map[num] = idx

for x in X:
    print(map[x], end=' ')
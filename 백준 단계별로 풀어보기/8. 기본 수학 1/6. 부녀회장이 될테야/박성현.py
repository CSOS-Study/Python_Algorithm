t = int(input())
kn = [(int(input()), int(input())) for _ in range(t)]
max_k = max(kn, key=lambda x:x[0])[0]
max_n = max(kn, key=lambda x:x[1])[1]
g = [list(range(1, max_n+1))] + [[1] * max_n for _ in range(max_k)]
for i in range(1, max_k+1):
    for j in range(1, max_n):
        g[i][j] = sum(g[i-1][:j+1])
for k, n in kn:
    print(g[k][n-1])

def chk(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global res
    if x == n:
        res += 1
    else:
        for i in range(n):
            row[x] = i
            if chk(x):
                dfs(x + 1)


n, res = int(input()), 0
row = [0] * n
dfs(0)
print(res)

def check(x):
    for i in range(x):
        if table[x] == table[i] or abs(table[x] - table[i]) == x - i:
            return False
    return True

def dfs(num):
    global result
    if num == n:
        result += 1
    else:
        for i in range(n):
            table[num] = i
            if check(num): dfs(num + 1)

n, result = int(input()), 0
table = [0] * n
dfs(0)
print(result)
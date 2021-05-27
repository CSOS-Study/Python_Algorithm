def dfs(a, b, c):
    global res
    cnt = 0
    for i in range(4):
        da = a + dx[i]
        db = b + dy[i]
        if 0 <= da < row and 0 <= db < col and case[da][db] not in c:
            dfs(da, db, c + case[da][db])
        else:
            cnt += 1
    if cnt == 4:
        res = max(res, len(c))
        return


row, col = map(int, input().split())
case = [list(input()) for _ in range(row)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = 0
dfs(0, 0, case[0][0])
print(res)


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

# 준수 풀
R, C = map(int, input().split())
board = [list(input())for _ in range(R)]
path = set()


def dfs(y, x):
    res = 1
    path.add(board[y][x])
    for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in path:
            res = max(res, 1 + dfs(ny, nx))
    path.remove(board[y][x])
    return res

print(dfs(0, 0))
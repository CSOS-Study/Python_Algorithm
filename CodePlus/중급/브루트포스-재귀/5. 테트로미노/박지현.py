import sys

d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 모든 좌표 이동 방향
dd = [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, -1)]]
# dfs로 탐색할 수 없는 ㅗ,ㅜ,ㅏ,ㅓ 는 notdfs()에서 따로 계산한다.

def notdfs(r, c):
    global answer
    for dir in dd:
        temp = paper[r][c]
        for idx in range(3):
            nr = r + dir[idx][0]
            nc = c + dir[idx][1]
            if 0 <= nr < N and 0 <= nc < M:
                temp += paper[nr][nc]
            else:
                break
        answer = max(answer, temp)

def dfs(r, c, total, visited):
    global answer
    if len(visited) == 4:
        answer = max(answer, total)
        return
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < N and 0 <= nc < M:
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                dfs(nr, nc, total + paper[nr][nc], visited)
                visited.pop()

N, M = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
for r in range(N):
    for c in range(M):
        dfs(r, c, paper[r][c], [(r, c)])
        notdfs(r, c)
print(answer)
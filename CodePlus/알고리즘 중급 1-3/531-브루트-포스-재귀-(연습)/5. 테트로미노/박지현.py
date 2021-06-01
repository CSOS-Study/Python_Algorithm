import sys

go = [(-1,0),(0,1),(1,0),(0,-1)] # 좌표 이동 전방향 표현
go_nodfs = [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, -1)]]
# dfs로 탐색할 수 없는 ㅗ,ㅜ,ㅏ,ㅓ 는 notdfs()에서 따로 계산

def dfs(y,x,total,visited):
    global mx
    if len(visited) == 4:
        mx = max(mx,total)
        return
    for i in range(4):
        yy = y + go[i][0]
        xx = x + go[i][1]
        if 0<=yy<n and 0<=xx<m:
            if (yy,xx) not in visited:
                visited.append((yy,xx))
                dfs(yy,xx,total+table[yy][xx],visited)
                visited.pop()

def no_dfs(y,x):
    global mx
    for i in go_nodfs:
        total = table[y][x]
        for j in range(3):
            yy = y + i[j][0]
            xx = x + i[j][1]
            if 0<=yy<n and 0<=xx<m: total += table[yy][xx]
            else: break
        mx = max(mx,total)

n, m = map(int,input().split())
table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
mx = 0
for y in range(n):
    for x in range(m):
        dfs(y,x,table[y][x],[(y,x)])
        no_dfs(y,x)
print(mx)
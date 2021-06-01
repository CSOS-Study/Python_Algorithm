
# n, m = 6, 2
# case = [['.', '#'],
#         ['.', '#'],
#         ['.', '#'],
#         ['o', '#'],
#         ['o', '#'],
#         ['#', '#']]


# print(coin)
def dfs(coin):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [[coin, 1]]
    visit = [coin]
    res = []
    while stack:
        [sa, sb], vcnt = stack.pop()
        for i, j in zip(dx, dy):
            tmp = []
            cnt = 0
            dsa = [sa[0] + i, sa[1] + j]
            dsb = [sb[0] + i, sb[1] + j]
            if [dsa, dsb] not in visit:
                try:
                    if case[dsa[0]][dsa[1]] == '#' and case[dsb[0]][dsb[1]] == '#':
                        continue
                except:
                    pass
                if 0 <= dsa[0] < n and 0 <= dsa[1] < m:
                    if case[dsa[0]][dsa[1]] != '#':
                        tmp.append([dsa[0], dsa[1]])
                    else:
                        tmp.append([sa[0], sa[1]])
                else:
                    cnt += 1
                if 0 <= dsb[0] < n and 0 <= dsb[1] < m:
                    if case[dsb[0]][dsb[1]] != '#':
                        tmp.append([dsb[0], dsb[1]])
                    else:
                        tmp.append([sb[0], sb[1]])
                else:
                    cnt += 1
                if cnt == 1:
                    print(tmp)
                    res.append(vcnt)
                elif len(tmp) == 2:
                    visit.append(tmp)
                    stack.extend([[tmp, vcnt + 1]])
    return res
n, m = map(int, input().split())
case = [list(input()) for _ in range(n)]
coin = []
for i in range(n):
    for j in range(m):
        if case[i][j] == 'o':
            coin.append([i, j])
visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
res = dfs(coin)
print(res if res else -1)

import sys

n = int(input())
case = list(map(int, input().split()))
op = list(map(int, input().split()))

max_res = -sys.maxsize
min_res = sys.maxsize


def dfs(cnt, res):
    global max_res, min_res
    if cnt == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    if op[0] > 0:
        op[0] -= 1
        dfs(cnt + 1, res + case[cnt])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(cnt + 1, res - case[cnt])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(cnt + 1, res * case[cnt])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(cnt + 1, int(res / case[cnt]))
        op[3] += 1


dfs(1, case[0])
print(max_res, min_res, sep='\n')

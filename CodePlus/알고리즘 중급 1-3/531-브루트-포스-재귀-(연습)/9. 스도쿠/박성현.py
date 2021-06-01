def chk(r, c):
    tmp = list(range(1, 10))
    for i in range(9):
        if case[r][i] in tmp:
            tmp.remove(case[r][i])
        if case[i][c] in tmp:
            tmp.remove(case[i][c])
    for i in range(3 * (r // 3), 3 * (r // 3) + 3):
        for j in range(3 * (c // 3), 3 * (c // 3) + 3):
            if case[i][j] in tmp:
                tmp.remove(case[i][j])
    return tmp


def sudoku(n):
    global flag
    if flag:
        return
    if n == len(zero):
        for i in case:
            print(' '.join(map(str, i)))
        flag = True
        return
    else:
        (i, j) = zero[n]
        for k in chk(i, j):
            case[i][j] = k
            sudoku(n + 1)
            case[i][j] = 0


case = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if not case[i][j]:
            zero.append((i, j))
flag = False
sudoku(0)
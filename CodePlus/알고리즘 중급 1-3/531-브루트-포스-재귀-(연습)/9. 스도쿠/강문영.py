sdo = [list(map(int, input().split())) for _ in range(9)]

emptySpace = [(i, j) for i in range(9) for j in range(9) if sdo[i][j] == 0]

def put_sdo_number(x, y):
    valid_number = [i + 1 for i in range(9)]

    for k in range(9):
        if sdo[x][k] in valid_number:
            valid_number.remove(sdo[x][k])
        if sdo[k][y] in valid_number:
            valid_number.remove(sdo[k][y])

    x_point = x // 3
    y_point = y // 3

    for i in range(x_point*3, (x_point+1)*3):
        for j in range(y_point*3, (y_point+1)*3):
            if sdo[i][j] in valid_number:
                valid_number.remove(sdo[i][j])
    return valid_number

already_done = False

def dfs(count):
    global already_done

    if already_done:
        return

    if count == len(emptySpace):
        for row in sdo:
            print(*row)
        already_done = True
        return

    (i, j) = emptySpace[count]
    check = put_sdo_number(i, j)

    for number in check:
        sdo[i][j] = number
        dfs(count + 1)
        sdo[i][j] = 0

dfs(0)

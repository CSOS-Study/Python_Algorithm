count = 0;
n = int(input())
board = [0] * 15


def is_put_okay(cdx):
    for i in range(cdx):
        if (board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i])):
            return 0
    return 1


def nqueen(cdx):
    global count
    if (cdx == n):
        count += 1
        return
    for i in range(n):
        board[cdx] = i
        if is_put_okay(cdx):
            nqueen(cdx + 1)


nqueen(0)
print(count)
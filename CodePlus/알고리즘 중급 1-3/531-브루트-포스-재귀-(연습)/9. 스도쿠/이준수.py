import collections
import sys

#주어진 board를 프린트합니다.
def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end=" ")
        print()

#zero좌표를 모두 없애면 board를 print한다.
def dfs(zero_list, board):
    #zero좌표가 없으므로 완성된 board이다. print하고 종료한다.
    if len(zero_list) == 0:
        print_board(board)
        exit()

    #미완성된 board이다. 0을 채워야한다. 0에 대해서 유효한 경우 다음 재귀를 호출한다.
    ny, nx = zero_list[0]
    for N in range(1, 10):
        if N not in col_check[nx] and N not in row_check[ny] and N not in box_check[(ny//3)*3 + nx//3]:
            col_check[nx].add(N)
            row_check[ny].add(N)
            box_check[(ny//3)*3 + nx//3].add(N)
            board[ny][nx] = N
            dfs(zero_list[1:], board)
            board[ny][nx] = 0
            col_check[nx].remove(N)
            box_check[(ny // 3) * 3 + nx // 3].remove(N)
            row_check[ny].remove(N)


#입력 받는법?
board = [[int(x) for x in sys.stdin.readline().split()] for _ in range(9)]
zero_list = [(y, x) for x in range(len(board[0])) for y in range(len(board)) if board[y][x] == 0]

col_check = collections.defaultdict(set)
row_check = collections.defaultdict(set)
box_check = collections.defaultdict(set)

for y in range(len(board)):
    for x in range(len(board[0])):
        col_check[x].add(board[y][x])
        row_check[y].add(board[y][x])
        box_check[(y//3)*3 + x//3].add(board[y][x])

dfs(zero_list,board)
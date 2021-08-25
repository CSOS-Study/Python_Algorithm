# ## bfs 문제이다. 중심을 기준으로 2*2 사각형이 형성되는지 확인필요
#
# def dfs(m, n, board):
#     confirm_point = [[(-1, -1), (-1, 0), (0, -1)], [(-1, 0), (-1, 1), (0, 1)]
#         , [(0, -1), (+1, -1), (1, 0)], [ (0, 1), (1, 0), (1, 1)]]
#
#     for y in range(m):
#         for x in range(n):
#             remove_target = set()
#             for check_points in confirm_point:
#                 temp = []
#                 for point in check_points:
#                     cpr_y = y + point[0]
#                     cpr_x = x + point[1]
#                     if 0 <= cpr_y < m and 0 <= cpr_x < n:
#                         if board[y][x] == board[cpr_y][cpr_x]:
#                             temp.append(str(cpr_y + cpr_x))
#
#                 if len(temp) == 3:
#                     for i in temp:
#                         remove_target.add(i)
#                     remove_target.add(str(y+x))
#
#     for del_point in remove_target:
#         del_y = del_point[0]
#         del_x = del_point[1]
#         board[del_y][del_x] = False
#
#
#
#
# def solution(m, n, board):
#     return answer

# def solution(m, n, board):
#     board = list(zip(*board))
#     check_point = [(-1, -1), (-1, 0), (0, -1), (0, 0)]
#     cnt = 0
#
#     x_point = set()
#     for y in range(1, n):
#         for x in range(1, m):
#             if board[y - 1][x - 1] == board[y - 1][x] == board[y][x - 1] == board[y][x] != False:
#                 x_point |= set([(y - 1, x - 1), (y - 1, x), (y, x - 1), (y, x)])
#
#     for j, i in x_point:
#         board[j][i] = "-" -> 튜플은 부련
련
#     for row in board:
#         print(row)


def solution(m, n, board):
    board = list(map(list, zip(*board)))
    check_point = [(-1, -1), (-1, 0), (0, -1), (0, 0)]
    cnt = 0

    while True:
        x_point = set()
        for y in range(1, n):
            for x in range(1, m):
                if board[y - 1][x - 1] == board[y - 1][x] == board[y][x - 1] == board[y][x] != False:
                    x_point |= set([(y - 1, x - 1), (y - 1, x), (y, x - 1), (y, x)])

        for j, i in x_point:
            board[j][i] = False

        for idx, row in enumerate(board):
            temp = [False] * row.count(False)
            board[idx] = temp + [x for x in row if x != False]

        cnt += len(x_point)
        if len(x_point) == 0:
            break

    return cnt
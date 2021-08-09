from collections import deque


def rotate(board, x1, y1, x2, y2):
    temp = deque()
    # 추출
    for dx in range(0, x2 - x1):
        temp.append(board[y1 - 1][(x1 - 1) + dx])  # 위줄 첫번째 부터 n-1번째까지
        temp.append(board[y2 - 1][(x1 - 1) + dx + 1])  # 아래줄 두번째부터 n번째까지

    for dy in range(0, y2 - y1):
        temp.append(board[(y1 - 1) + dy + 1][x1 - 1])  # 첫번째 열에서 두번째부터 n번째까지
        temp.append(board[(y1 - 1) + dy][x2 - 1])  # 마지막 열에서 첫번째부터 n-1번째까지

    min_score = min(temp)

    # 추출된 원소 차례대로 삽입
    for change_dx in range(1, x2 - x1 + 1):
        board[y1 - 1][x1 - 1 + change_dx] = temp.popleft()  # 위줄 두번째부터 n번째까지로 바꿈
        board[y2 - 1][x1 - 1 + change_dx - 1] = temp.popleft()  # 아래줄 첫번째부터 n-1번째까지로 바꿈

    for change_dy in range(1, y2 - y1 + 1):
        board[(y1 - 1) + change_dy - 1][x1 - 1] = temp.popleft()
        board[(y1 - 1) + change_dy][x2 - 1] = temp.popleft()

    return min_score, board


def solution(rows, columns, queries):
    result = []
    board = [[x + (y - 1) * columns for x in range(1, columns + 1)] for y in range(1, rows + 1)]

    for i in queries:
        y1, x1 = i[0], i[1]
        y2, x2 = i[2], i[3]

        min, board = rotate(board, x1, y1, x2, y2)

        result.append(min)

    return result
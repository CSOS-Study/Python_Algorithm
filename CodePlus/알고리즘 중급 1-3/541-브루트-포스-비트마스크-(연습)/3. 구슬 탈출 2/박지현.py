import collections

def move_marble(marble_position, dy, dx):
    y, x = marble_position
    moved_num = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        moved_num += 1
        y += dy
        x += dx
    return y, x, moved_num

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
red_position = tuple()
blue_position = tuple()
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            red_position = (y, x)
        elif board[y][x] == 'B':
            blue_position = (y, x)

Q = collections.deque()
Q.append((red_position, blue_position))
path = set((red_position, blue_position))

cnt = 0
# 현재의 움직임이 11번째일때 while문을 탈출한다.
while Q and cnt < 10:
    cnt += 1
    for _ in range(len(Q)):
        red_position, blue_position = Q.popleft()

        for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
            n_red_y, n_red_x, n_moved_red = move_marble(red_position, dy, dx)
            n_blue_y, n_blue_x, n_moved_blue = move_marble(blue_position, dy, dx)

            if board[n_blue_y][n_blue_x] == 'O':
                continue

            elif board[n_red_y][n_red_x] == 'O':
                print(cnt)
                exit()

            if n_red_y == n_blue_y and n_red_x == n_blue_x:
                if n_moved_red > n_moved_blue:
                    n_red_y += -dy
                    n_red_x += -dx
                else:
                    n_blue_y += -dy
                    n_blue_x += -dx

            n_marble_position = ((n_red_y, n_red_x), (n_blue_y, n_blue_x))
            if n_marble_position not in path:
                path.add(n_marble_position)
                Q.append(n_marble_position)

print(-1)
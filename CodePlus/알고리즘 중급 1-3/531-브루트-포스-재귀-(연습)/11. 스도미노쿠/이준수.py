import collections
import copy
from itertools import permutations, combinations


def make_init_board():
    #판을 만든다.
    board = [[0 for _ in range(9)] for _ in range(9)]
    table = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
    }
    #N개의 도미노을 채운다.
    N = int(input())
    if N == 0:
        exit()

    for _ in range(N):
        num1, position1, num2, position2 = input().split()
        y1, x1 = table[position1[0]], int(position1[1])-1
        y2, x2 = table[position2[0]], int(position2[1])-1
        board[y1][x1] = int(num1)
        board[y2][x2] = int(num2)

    #9개의 숫자를 채운다.
    for num, position in enumerate(input().split()):
        y, x = table[position[0]], int(position[1])-1
        board[y][x] = num + 1

    return board

def brute_force(board):
    if len(zero_check) == 0:
        #print(board)
        return True

    #유효한 위치에서 하나를 뽑음
    for y, x in zero_check:
        #또다른 유효한 위치를 찾는 상태
        for dy, dx in (0, +1), (+1, 0):
            ny = y + dy
            nx = x + dx
            if (ny,nx) in zero_check:
                #y, x, ny, nx 모두 유효한 위치임.
                #해당위치에 어떤 숫자가 맞는지 판단할꺼임.
                #y,x에 맞는 숫자. (들어가도 되는 숫자)
                valid_num1 = col_check[x] & row_check[y] & box_check[(y // 3) * 3 + x // 3]
                #ny,nx에 맞는 숫자. (들어가도 되는 숫자)
                valid_num2 = col_check[nx] & row_check[ny] & box_check[(ny // 3) * 3 + nx // 3]
                #도미노로서의 결합
                for num1 in valid_num1:
                    for num2 in valid_num2 & dominos[num1]:
                        #같으면 안되고 사용했던 도미노여도 안됨
                        #도미노에는 사용가능한 도미노들이 들어있음
                        board[y][x] = num1
                        col_check[x].remove(num1)
                        row_check[y].remove(num1)
                        box_check[(y // 3) * 3 + x // 3].remove(num1)

                        board[ny][nx] = num2
                        col_check[nx].remove(num2)
                        row_check[ny].remove(num2)
                        box_check[(ny // 3) * 3 + nx // 3].remove(num2)

                        dominos[num1].remove(num2)
                        dominos[num2].remove(num1)

                        zero_check.remove((y,x))
                        zero_check.remove((ny,nx))

                        if brute_force(board):
                            return True

                        board[y][x] = 0
                        col_check[x].add(num1)
                        row_check[y].add(num1)
                        box_check[(y // 3) * 3 + x // 3].add(num1)

                        board[ny][nx] = 0
                        col_check[nx].add(num2)
                        row_check[ny].add(num2)
                        box_check[(ny // 3) * 3 + nx // 3].add(num2)

                        dominos[num1].add(num2)
                        dominos[num2].add(num1)

                        zero_check.append((y, x))
                        zero_check.append((ny, nx))

    return False

cnt = 1
while True:
    #초기 보드임
    board = copy.deepcopy(make_init_board())
    #각각의 체크는 각 포지션에서 가능한 번호를 담고있음.
    col_check = collections.defaultdict(set)
    row_check = collections.defaultdict(set)
    box_check = collections.defaultdict(set)
    dominos = collections.defaultdict(set)
    for idx in range(9):
        col_check[idx] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        row_check[idx] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        box_check[idx] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        dominos[idx+1] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        dominos[idx+1].remove(idx+1)

    zero_check = list()

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                zero_check.append((y, x))
            else:
                col_check[x].remove(board[y][x])
                row_check[y].remove(board[y][x])
                box_check[(y//3)*3 + x//3].remove(board[y][x])

    brute_force(board)

    print(f'Puzzle {cnt}')
    for i in range(9):
        print(*board[i], sep='')
    cnt += 1
N, M = map(int,input().split())
board = [input() for _ in range(N)]

case = "WB"
res = 65
white = 0
black = 0
for y in range(N-8+1):
    for x in range(M-8+1):
        white = 0
        black = 0
        for i in range(8):
            for j in range(8):
                #white
                if case[(i+j) % 2] != board[y+i][x+j]:
                    white += 1

                #black
                if case[(i + j + 1) % 2] != board[y+i][x+j]:
                    black += 1
        res = min(res,white,black)

print(res)
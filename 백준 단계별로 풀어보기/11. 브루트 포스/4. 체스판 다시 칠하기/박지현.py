N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7): # 8*8을 뽑아야하니까 시작 인덱스를 -7로 설정한 것
        b_to_W, w_to_B = 0, 0
        for k in range(i,i+8):
            for l in range(j,j + 8): # 8*8 다 돌면서 체크

                # 짝/홀수 인덱스는 B이든 W이든 동일한 색을 갖는다.
                if (k + l) % 2 == 0:
                    if board[k][l] == 'B': b_to_W +=1
                    if board[k][l] == 'W': w_to_B +=1
                else:
                    if board[k][l] == 'W': b_to_W +=1
                    if board[k][l] == 'B': w_to_B +=1
        repair.append(b_to_W)
        repair.append(w_to_B)
print(min(repair))
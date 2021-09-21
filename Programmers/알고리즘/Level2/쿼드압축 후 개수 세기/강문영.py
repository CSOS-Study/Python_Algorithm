# divide(r, c, n // 2)
# divide(r + n // 2, c, n // 2)
# divide(r, c + n // 2, n // 2)
# divide(r + n // 2, c + n // 2, n // 2)
# 이게 과연 다 커버가 될까?
# 커버가 된다. 왜냐면 하나의 직사각형이 포함이 안되면 그 내부를 4등분 하기 때문이다.
# 첫번째 케이스부터 확인한다.
# 하나만 확인하고, 아니면 그 경우를 4분할 하도록 넘겨준다.
result= [0,0]

def bfs(arr, x, y, n):
    global result
    temp = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if temp != arr[i][j]:
                bfs(arr, x+n//2, y, n//2)
                bfs(arr, x, y+n//2, n//2)
                bfs(arr, x, y, n//2)
                bfs(arr, x+n//2, y+n//2, n//2)
                return
    else:
        result[temp] +=1

def solution(arr):
    global result
    bfs(arr, 0,0,len(arr))
    return result
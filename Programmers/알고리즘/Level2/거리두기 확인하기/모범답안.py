from collections import deque

d = ((0, 1), (1, 0), (-1, 0), (0, -1))
SIZE = 5


def make_maps(place):
    arr = []
    men = []
    for i, string in enumerate(place):
        for j, ch in enumerate(string):
            if ch == 'P': men.append((i, j))

        arr.append(list(string))

    return arr, men


def isin(y, x): # 전체 5*5 배열에 들어오는지 확인
    if -1 < y < SIZE and -1 < x < SIZE: return True
    return False


def bfs(arr, sy, sx):
    q = deque()
    q.append((sy, sx)) # 큐에 받은 P점의 좌표를 집어넣기
    table = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]
    table[sy][sx] = 0 # 그 위치를 제외한 나머지 5*5 배열 -1, 그 위치는 0으로 설정

    while q: # q는 1개인데..? 아무튼
        y, x = q.popleft() # q에서 하나를 꺼낸다. (가장 앞쪽에서 꺼내는 것)

        for dy, dx in d: # d는 q점에서 상하좌우 인 곳
            ny = y + dy # 각각 상하 좌우를 확인한다.
            nx = x + dx

            if not isin(ny, nx): continue # 5*5 배열에 들어오는지 확인하고 없으면 패스
            if arr[ny][nx] != 'X' and table[ny][nx] == -1: # 파티션이 아니고, 아직 방문을 안한 점이라고 하면 # 만약 이게 거리두기를 지키려면, 거리가 2여야 함
                # 아.. 다른 P가 아닐때까지 1씩 가중치를 준다. 파티션이면 이미 거리두기OK임으로 패스이고, 아니면 거리 +=1
                # 근데 내가 궁금한 점은 table[ny][nx] == -1 이면, 이전에 방문한 점은 안되니까 거리두기 2가 성립이 안되는거 아님?
                # 그러니까 즉 모두 0이 되는거 아닌가?
                table[ny][nx] = table[y][x] + 1 # 원래 점에서 1만큼 떨어져있음으로, 거리 1을 더해준다.
                # 아 그러니까 원래 점을 기준으로 BFS를 돌기 때문에 원래 점 기준으로 그 다음점은 +2가 되겠다.
                q.append((ny, nx)) # 큐에 집어넣는다.

    return table


def solution(places):
    answer = []
    for place in places:
        arr, men = make_maps(place)
        ok = True

        for man in men:
            table = bfs(arr, man[0], man[1]) # P점의 좌표를 인자로 받음(1개씩)
            for other_man in men:
                if man != other_man: # 다시 P점들 중 하나를 뽑고, 기존에 비교하려던 점과 같지 않으면
                    y = other_man[0] #그것을 x,y에 넣는다.
                    x = other_man[1]
                    if -1 < table[y][x] <= 2: # 그리고, 위에서 bfs를 돌아서  거리두기 성립이 안되면
                        ok = False # 폴스로 설정해둠
                        break

            if not ok: break # 그래서, 해당 P점이 다른 P점과 거리두기가 아니면 break

        if ok:
            answer.append(1)
        else:
            answer.append(0)

    return answer
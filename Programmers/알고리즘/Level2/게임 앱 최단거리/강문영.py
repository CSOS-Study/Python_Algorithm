from collections import deque


def solution(maps): 
    # 일단 전체 길에 포함여부 확인
    # 이미 갔던 길은 다시 들어가면 노노링
    # 현재 위치에서 상하좌우를 확인하되, 해당 위치가 0이면 안됨
    confirm_point = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # dy, dx
    queue = deque()
    queue.append((0, 0))
    graph = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    graph[0][0] = 1

    while queue:
        start_point = queue.popleft()
        for dy, dx in confirm_point:
            y = dy + start_point[0]
            x = dx + start_point[1]

            if -1 < y < len(maps) and -1 < x < len(maps[0]) and maps[y][x] == 1:  # 전체 map에 포함되는지?
                if graph[y][x] == -1:
                    graph[y][x] = graph[start_point[0]][start_point[1]] + 1
                    queue.append((y, x))

    ## 막혔던 점
    ## 2갈래가 나뉘어지면, 이후에는 어떻게 갈라서 코드를 작성할지 몰랐음
    ## 그걸 graph가 해줌
    ## 인접행렬(graph)를 선언하고, 이것을 갱신하는 방식이 아직 완벽하게 이해가 안됨

    return graph[-1][-1]
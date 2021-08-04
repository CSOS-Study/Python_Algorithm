from collections import deque


def extract_place_and_p(place):
    total_place = []
    p_place = []
    for i_idx, i in enumerate(place):
        temp = list(i)
        for j_idx, j in enumerate(i):
            if j == "P":
                p_place.append((i_idx, j_idx))
        total_place.append(temp)

    return total_place, p_place


def is_valid_point(x, y):
    if -1 < x < 5 and -1 < y < 5:
        return True
    return False


compare_point = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(total_distance_table, x, y):
    deque_test = deque()
    deque_test.append((x, y))
    distacne_table_point = [[-1 for _ in range(5)] for _ in range(5)]
    distacne_table_point[x][y] = 0

    while deque_test:
        know_point = deque_test.popleft()

        for dx, dy in compare_point:
            cpr_x = know_point[0] + dx
            cpr_y = know_point[1] + dy

            if is_valid_point(cpr_x, cpr_y):
                if distacne_table_point[cpr_x][cpr_y] == -1 and total_distance_table[cpr_x][cpr_y] != "X":
                    distacne_table_point[cpr_x][cpr_y] = distacne_table_point[know_point[0]][know_point[1]] + 1
                    deque_test.append((cpr_x, cpr_y))

    return distacne_table_point


def solution(places):
    result = []
    for place in places: # 대기실 하나씩 확인
        target_table, p_place = extract_place_and_p(place) # 대기실 인원 배치 명단과 인터뷰 대상자가 앉아있는 포인트
        is_pass = True
        for point in p_place:  # P 포인트 점을 하나씩 꺼내서 테이블을 만들기
            compare_table = bfs(target_table, point[0], point[1])
            for diff_point in p_place:
                if point != diff_point:
                    if -1 < compare_table[diff_point[0]][diff_point[1]] <= 2:
                        is_pass = False
                        break

            if not is_pass:
                break

        if not is_pass:
            result.append(0)
        else:
            result.append(1)

    return result



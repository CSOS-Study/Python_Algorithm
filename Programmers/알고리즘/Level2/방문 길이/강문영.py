def solution(dirs):
    direction_weight = {
        "U": [1, 0],
        "D": [-1, 0],
        "R": [0, 1],
        "L": [0, -1]
    }

    passed_road = set()
    start_point = [0, 0]

    for dir in dirs:
        dx = start_point[0] + direction_weight[dir][0]
        dy = start_point[1] + direction_weight[dir][1]

        if -6 < dx < 6 and -6 < dy < 6:
            passed_road.add(tuple(sorted((str(start_point[0]) + str(start_point[1]), str(dx) + str(dy)))))
            start_point[0] = dx
            start_point[1] = dy

    return len(passed_road)
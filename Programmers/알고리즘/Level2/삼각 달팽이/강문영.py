def solution(n):
    # 1
    res = [[0] * n for _ in range(n)]
    answer = []
    dy, dx = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                dy += 1
            elif i % 3 == 1:
                dx += 1
            else:
                dy -= 1
                dx -= 1

            res[dy][dx] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer
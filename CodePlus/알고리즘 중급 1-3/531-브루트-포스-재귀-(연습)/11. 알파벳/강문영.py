r, c = map(int,input().split())

board = [list(input().split()) for _ in range(r)]

# def is_passed(x, y):


def dfs(count):
    passed_list = []

    # if count == len(emptySpace):
    #     for row in sdo:
    #         print(*row)
    #     already_done = True
    #     return
    #
    # (i, j) = emptySpace[count]
    # check = put_sdo_number(i, j)

    for i in range(r):
        for j in range(c):
            passed_list.append()

    for number in check:
        sdo[i][j] = number
        dfs(count + 1)
        sdo[i][j] = 0

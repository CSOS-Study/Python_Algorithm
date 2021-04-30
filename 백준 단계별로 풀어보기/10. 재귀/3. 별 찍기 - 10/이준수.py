def make_pattern(y, x, n, star) -> None:
    if (n == 1):
        star[y][x] = "*"
        return

    for i in range(y, y + n, n // 3):
        for j in range(x, x + n, n // 3):
            if not (i == y + n // 3 and j == x + n // 3):
                make_pattern(i, j, n // 3, star)
    return


def print_pattern(n, star) -> None:
    for y in range(n):
        for x in range(n):
            print(star[y][x], end="")
        print()


n = int(input())
star = [[' ' for x in range(n)] for y in range(n)]
make_pattern(0, 0, n, star)
print_pattern(n, star)

# 배열 선언 방법
# https://yechoi.tistory.com/52

# COLUM : 가로 길이
# ROW : 세로 길이
# board = [[0 for i in range(COLUM)] for j in range(ROW)]

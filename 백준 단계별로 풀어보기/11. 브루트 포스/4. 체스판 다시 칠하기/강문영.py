import sys
def main():

    n, m = map(int, input().split())

    all_line = []
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        all_line.append(list(line))

    min = 50 * 50
    for i in range(n - 7):
        for j in range(m - 7):
            check_value = check(i, j, all_line)
            if check_value < min:
                min = check_value

    print(min)


def check(n, m, array):

    cnt_B = 0
    cnt_W = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if "B" != array[n + i][m + j]:
                    cnt_B += 1
                else:
                    cnt_W += 1
            elif (i + j) % 2 == 1:
                if "B" == array[n + i][m + j]:
                    cnt_B += 1
                else:
                    cnt_W += 1

    return cnt_B if cnt_B < cnt_W else cnt_W

main()
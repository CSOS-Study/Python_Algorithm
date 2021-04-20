def solve_3(n):
    if n < 100:
        print(n)
    else:
        han = 0
        for i in range(100, n + 1):
            sn = str(i)
            if int(sn[2]) - int(sn[1]) == int(sn[1]) - int(sn[0]):
                han += 1
        print(99 + han)

solve_3(1000)
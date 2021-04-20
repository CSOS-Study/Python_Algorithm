def solve_2():
    l = [0] * 10000
    for i in range(1, 10001):
        chk = i
        for j in str(i):
            chk += int(j)
        if chk - 1 >= 10000: continue
        l[chk - 1] = 1
    for i in range(len(l)):
        if l[i] == 0: print(i + 1)

solve_2()
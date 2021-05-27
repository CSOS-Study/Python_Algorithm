def sol(case, tmp = 0):
    if len(case)<3:
        global res
        res = max(res, tmp)
    for i in range(1, len(case)-1):
        tmp += case[i-1]*case[i+1]
        chk = case.pop(i)
        sol(case, tmp)
        case.insert(i, chk)
        tmp -= case[i - 1] * case[i + 1]


n, res = int(input()), 0
sol(list(map(int, input().split())))
print(res)

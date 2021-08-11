def sol(pay=0, d=0):
    global res
    tmp_case = list(filter(lambda x: x[2] >= d, case))
    if not tmp_case:
        res = max(res, pay)
        return
    for a, b, c in tmp_case:
        sol(pay + b, a + c)


n, res = int(input()), 0
case = list(filter(lambda x: (x[0] + x[2]) < n + 1, [list(map(int, input().split())) + [i] for i in range(n)]))
sol()
print(res)

def generator(n):
    res = n
    for _ in str(n):
        res += int(_)
    if res > 10000:
        res = 0
    return res

res = [0] * 10001
for i in range(1,10000):
    res[generator(i)] = 1
for _ in range(10001):
    if(res[_]==0):
        print(_)
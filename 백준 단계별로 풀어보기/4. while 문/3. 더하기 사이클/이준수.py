init = int(input())
_ = init
res = 0

while True:
    _ = (_ % 10) * 10 + (_ // 10 + _ % 10) % 10
    res += 1
    if (_ == init):
        break

print(res)
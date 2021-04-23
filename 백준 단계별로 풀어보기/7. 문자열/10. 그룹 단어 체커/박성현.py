n = int(input())
for i in [str(input()) for _ in range(n)]:
    chk = []
    for j in i:
        if j in chk:
            if j == chk[-1]: continue
            n -= 1
            break
        else:
            chk.append(j)
print(n)
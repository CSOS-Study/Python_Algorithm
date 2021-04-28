N = int(input())
c = 0
for i in range(N//5, -1, -1):
    if not (N-i*5) % 3:
        c += i + int((N-i*5)/3)
        break
print((not c) and -1 or c)

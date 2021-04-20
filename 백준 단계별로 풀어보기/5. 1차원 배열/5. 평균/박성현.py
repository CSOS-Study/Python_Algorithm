n, l, avg = int(input()), list(map(int, input().split())), 0
m = max(l)
for i in l:
    avg += i / m * 100
print(avg / n)

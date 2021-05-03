def stars(n):
    arr = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            arr.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            arr.append(n[i % len(n)] * 3)
    return (list(arr))


star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)

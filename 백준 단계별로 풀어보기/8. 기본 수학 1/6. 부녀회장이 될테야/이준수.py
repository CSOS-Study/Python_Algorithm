T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    floor = list(range(n+1)) # [range(n+1)]과 다르다.
    for y in range(1, k+1):
        for x in range(1, n+1):
           floor[x] += floor[x-1]
    print(floor[n])
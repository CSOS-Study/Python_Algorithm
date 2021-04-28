T = int(input())
for _ in range(T):
    source, destination = map(int, input().split())
    d = destination - source
    i = 1
    while True:
        if i ** 2 - i + 1 <= d and d <= i**2 + i :
            if d <= i ** 2 :
                print(2*i - 1)
            else:
                print(2*i)
            break
        i+=1
x = y = 0
for _ in range(3):
    a,b = map(int,input().split())
    x ^= a
    y ^= b
print(x,y)
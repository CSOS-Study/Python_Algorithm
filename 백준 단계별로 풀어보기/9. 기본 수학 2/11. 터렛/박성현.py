for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r3 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if r3==0 and r1==r2:
        print(-1)
    elif r3==r1+r2 or r3==abs(r1-r2):
        print(1)
    elif abs(r1-r2) < r3 < r1+r2:
        print(2)
    else:
        print(0)
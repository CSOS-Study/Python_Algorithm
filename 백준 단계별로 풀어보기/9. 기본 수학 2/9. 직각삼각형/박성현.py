while True:
    a, b, c = sorted(map(int, input().split()))
    if not a:
        break
    elif a**2+b**2==c**2:
        print('right')
    else:
        print('wrong')
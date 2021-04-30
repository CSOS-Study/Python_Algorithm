while True:
    triangle_sides = list(map(int,input().split()))
    if not triangle_sides[0] and not triangle_sides[1] and not triangle_sides[2]:
        break

    triangle_sides.sort()
    if triangle_sides[2]**2 == triangle_sides[0]**2 + triangle_sides[1]**2:
        print("right")
    else:
        print("wrong")

'''
base case : 0 0 0 인경우.
정렬후 가장 긴 변 ^2 = 나머지 각 변 **2 의합
'''
while True:
    triangle_sides = list(map(int,input().split()))
    if not triangle_sides[0] and not triangle_sides[1] and not triangle_sides[2]:
        break

    triangle_sides.sort()
    if triangle_sides[2]**2 == triangle_sides[0]**2 + triangle_sides[1]**2:
        print("right")
    else:
        print("wrong")
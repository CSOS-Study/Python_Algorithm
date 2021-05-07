'''
move_ring : n개의 ring을 from에서 to로 옮긴다. from / to / other
초기값 : from : 1 to : 3 other : 2

1에 있는 맨밑을 제외한 모든것들을 2에 옮긴다. move_ring(n - 1, source, other, destination)
1에 있는 하나를 3에 옮긴다.
2에 있는 모든것들을 3에 옮긴다.
'''

route = []
def move_ring(n: int, source: int, destination: int, other: int):
    if n == 0:
        return 0

    res = 0
    res += move_ring(n - 1, source, other, destination)

    route.append((source, destination))
    res += 1

    res += move_ring(n - 1, other, destination, source)
    return res


n = int(input())
print(move_ring(n, 1, 3, 2))

for i in route:
    print(i[0], i[1])
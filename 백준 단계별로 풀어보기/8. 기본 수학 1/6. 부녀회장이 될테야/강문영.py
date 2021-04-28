n = int(input())

# def people(floor, room):
#     if floor == 0:
#         return room
#     total_people = 0
#     for i in range(room+1):
#         total_people += people(floor - 1, i)
#     return total_people

for _ in range(n):
    floor = int(input())
    room = int(input())
    v = [i for i in range(1,room+1)]
    for _ in range(floor):
        for j in range(1,room):
            v[j] += v[j-1]
    print(v[room-1])

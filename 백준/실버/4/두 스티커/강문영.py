from itertools import combinations

h, w = map(int, input().split())
n = int(input())

sticker_llist = []
result = []

for _ in range(n):
    sticker_llist.append(list(map(int, input().split())))

for a, b in combinations(sticker_llist, 2):
    x1, y1, x2, y2 = a[0], a[1], b[0], b[1]

    if x1 + x2 <= h and y1 <= w and y2 <= w:
        result.append((x1 * y1) + (x2 * y2))
    elif x1 + x2 <= w and y1 <= h and y2 <= h:
        result.append((x1 * y1) + (x2 * y2))
    elif y1+ y2 <= w and x1 <= h and x2 <= h:
        result.append((x1 * y1) + (x2 * y2))
    elif y1 + y2 <= h and x1 <= w and x2 <= w:
        result.append((x1 * y1) + (x2 * y2))
    elif x1 + y2 <= h and y1 <= w and x2 <= w:
        result.append((x1 * y1) + (x2 * y2))
    elif x1 + y2 <= w and y1 <= h and x2 <= h:
        result.append((x1 * y1) + (x2 * y2))

if len(result) == 0:
    print(0)
else:
    print(max(result))

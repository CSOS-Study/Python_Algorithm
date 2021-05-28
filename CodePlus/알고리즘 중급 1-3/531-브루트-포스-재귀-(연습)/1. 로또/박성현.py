from itertools import combinations

while True:
    case = list(map(int, input().split()))
    if not case[0]: break
    for i in combinations(case[1:], 6):
        print(' '.join(map(str, i)))
    print()
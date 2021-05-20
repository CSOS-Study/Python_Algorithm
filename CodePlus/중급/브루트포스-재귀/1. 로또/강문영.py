from itertools import combinations
while True:
    n_list = list(input().split())

    if n_list[0] == '0' :
        break
    n, n_list = n_list[0],n_list[1:]

    for i in combinations(n_list,6):
        print(' '.join(list(i)))
    print()

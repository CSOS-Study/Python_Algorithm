from itertools import combinations

dominos = set()
for n1, n2 in combinations(range(1, 10),2):
    print(n1, n2)
    dominos.add((n1, n2))
from itertools import combinations

n, m = map(int, input().split())
case = []
for i in combinations(list(map(int, input().split())), 3):
    case.append(sum(i))
print(sorted(list(filter(lambda x:x<=m, case)), reverse=True)[0])
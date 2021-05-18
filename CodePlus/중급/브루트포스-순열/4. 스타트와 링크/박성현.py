from itertools import combinations, permutations

n=int(input())
case=[list(map(int, input().split())) for _ in range(n)]
team=list(combinations(range(n), n//2))
res=[]
for a, b in zip(team[:len(team)//2], team[-1:len(team)//2-1:-1]):
    start, link = 0, 0
    for i, j in permutations(a, 2):
        start+=case[i][j]
    for i, j in permutations(b, 2):
        link+=case[i][j]
    res.append(abs(start-link))
print(min(res))
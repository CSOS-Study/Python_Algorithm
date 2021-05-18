from itertools import combinations, permutations
import sys

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
all_team = set(range(N))

res = sys.maxsize
for team in combinations(range(N), N//2):
    if team[0] != 0:
        break

    start_team = 0
    for ability in permutations(team, 2):
        start_team += board[ability[0]][ability[1]]

    link_team = 0
    team = all_team - set(team)
    for ability in permutations(team, 2):
        link_team += board[ability[0]][ability[1]]

    res = min(res, abs(start_team-link_team))

print(res)
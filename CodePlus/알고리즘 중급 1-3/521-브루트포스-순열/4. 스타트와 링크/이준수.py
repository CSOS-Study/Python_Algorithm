from itertools import combinations, permutations
import sys

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
all_team = list(combinations(range(N), N//2))
start_team = all_team[:len(all_team)//2:]
link_team = all_team[-1:len(all_team)//2-1:-1]

res = sys.maxsize

for start_team, link_team in zip(start_team, link_team):
    start_team_ability = 0
    for ability in permutations(start_team, 2):
        start_team_ability += board[ability[0]][ability[1]]

    link_team_ability = 0
    for ability in permutations(link_team, 2):
        link_team_ability += board[ability[0]][ability[1]]

    res = min(res, abs(start_team_ability-link_team_ability))

print(res)

# 0번 선수가 start_team에 잇는거만 구하면됨.
# 0번선수가 link_team
# 조합을 둘로 나누는법
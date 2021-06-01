'''
문제
게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다.
게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. (플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동)
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.
뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

제약 조건
만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.
사다리나 뱀을 이용해 이동한 칸의 번호는 원래 번호와 다르다.
1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다.
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
항상 100번 칸에 도착할 수 있는 입력만 주어진다.

입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.
'''
import collections

N, M = map(int, input().split())
#모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
skip = dict()
for _ in range(N+M):
    key, value = map(int, input().split())
    skip[key] = value

Q = collections.deque()
Q.append(1)
path = set()
path.add(1)
dice_cnt = 0
while Q:
    dice_cnt += 1
    for _ in range(len(Q)):
        position = Q.popleft()
        for dice in range(1,6+1):
            new_position = position + dice
            #만약 주사위를 굴려서 이동한 결과가 100번 칸을 넘어간다면 이동할 수 없다.
            if new_position > 100:
                continue

            # 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다.
            # 정답에 도달한 경우 주사위를 굴린 횟수를 반환하고 종료한다.
            if new_position == 100:
                print(dice_cnt)
                exit()

            #사다리나 뱀에 존재할경우. 해당 좌표로 이동한다.
            if new_position in skip:
                new_position = skip[new_position]

            #해당 경로가 발견되지 않았다면
            if new_position not in path:
                path.add(new_position)
                Q.append(new_position)

            #발견되었다면 Q에 넣지 않는다.

#항상 100번 칸에 도착할 수 있는 입력만 주어진다. -> Q가 empty인 경우는 없다.

#skip = {key: value for key, value in map(int, input().split()) for _ in range(N+M)} #뱀 / 사다리 정보 저장.
#https://bio-info.tistory.com/40
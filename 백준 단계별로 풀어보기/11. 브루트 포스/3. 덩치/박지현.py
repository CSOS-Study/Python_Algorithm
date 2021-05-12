'''
(몸무게,키) = (X,Y)로 입력 받는다.
X와 Y 둘다 다른 사람의 X, Y보다 크다면 덩치가 크다고 한다.
덩치 등수는 '자신보다 덩치가 큰 사람의 수 +1'등 으로 매긴다.

* 덩치가 가장 큰 사람은 1등
* 자신보다 큰 덩치가 1명 있는 사람은 2등 ... 이런식으로 함
'''
N, d_lst, rank = int(input()), [], []
for i in range(N):
    dungch = list(map(int, input().split()))
    d_lst.append(dungch)
for i in range(len(d_lst)):
    cnt = 1
    for j in range(len(d_lst)):
        if d_lst[i][0] < d_lst[j][0] and d_lst[i][1] < d_lst[j][1]:
            cnt += 1
    rank.append(cnt) # i의 등수를 기록
for i in rank:
    print(i, end=' ')
'''
카드의 개수 N
N개의 카드 중 3장의 합이 M을 넘기면 안됨

합이 M에 가장 가까워질 수 있는 카드 3장을 찾고, 그 합을 출력
'''
N, M = map(int, input().split())
card_lst, result_lst = list(map(int,input().split())), []

for a in range(N-2):
    for b in range(a+1,N-1):
        two_sum = card_lst[a] + card_lst[b]
        if two_sum >= M: continue #이럴 경우 아래 for를 굳이 돌릴 필요 없음
        for c in range(b+1,N):
            result = two_sum + card_lst[c]
            if result <= M : result_lst.append(result)
            else : pass

print(max(result_lst))
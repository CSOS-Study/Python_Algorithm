'''
함수이용
from itertools import combinations

while True:
    N, *german_lotto = list(map(int,input().split()))
    if N == 0:
        break
    for case in combinations(german_lotto, 6):
        print(*case)
    print()
'''
#idx를 뽑아 case인 경우(길이가 6인경우) 출력한다.
def print_case(idx:int, case:list, german_lotto:list):
    if idx == len(german_lotto):
        if len(case) == 6:
            print(*case)
        return

    print_case(idx+1, case+[german_lotto[idx]], german_lotto)
    print_case(idx+1, case, german_lotto)


while True:
    N, *german_lotto = list(map(int,input().split()))
    if N == 0:
        break

    print_case(0, [], german_lotto)
    print()
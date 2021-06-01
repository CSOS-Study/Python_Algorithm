'''
TestCase로 받은 k개의 수에서 6개만 뽑을 때, 가능한 모든 경우를 출력.
'''
import sys, itertools

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0: break  # 입력 종료
    del num[0]
    for i in list(itertools.combinations(num,6)):
        print(*i)
    print()

# import sys
#
# def backtracking(check,pass_lst,inx):
#     if len(pass_lst) == 6:
#         print(*pass_lst) #unpacking
#         return # 재귀 안에서 return -> 그 다음 line 실행
#
#     for i in range(inx, len(num)):
#         print(i)
#         if check[i]==False: # 아직 안쓴 원소라면,
#             check[i]=True
#             pass_lst.append(num[i])
#             backtracking(check,pass_lst,i+1)
#
#             pass_lst.pop() #맨 뒤의 수부터 지운다. -> 그 다음 수를 체크하기 위해
#             check[i] = False
#
# while True:
#     num = list(map(int,sys.stdin.readline().split()))
#     if num[0] ==0: break #입력 종료
#     del num[0]
#
#     check = [False] * len(num) # 각 index의 원소를 check 했는지 안했는지 저장
#     pass_lst = [] # 6개짜리 경로(?)
#     backtracking(check,pass_lst,0)

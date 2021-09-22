# def check_is_rectan(board, n):
#     is_rec = False
#
#     for i in range(0, len(board), n):
#         for j in range(0, len(board), n):
#             is_okay = True
#             for x in range(i, i + n):  # 여기부터 아래 루프까지가 하나의 정사각형
#                 for y in range(j, j + n):
#                     if -1 < x < len(board) and -1 < y < len(board):
#                         if board[x][y] != 1:
#                             is_okay = False
#                             break
#                     else:
#                         is_okay = False
#                         break
#                 if not is_okay:
#                     break
#         else:
#             is_rec = True
#
#     if is_rec:
#         return True
#     return False
#
#
# def solution(board):
#     max = -111
#     for n in range(1, len(board) + 1):
#         if check_is_rectan(board, n):
#             if n * n > max:
#                 max = n * n
#     return max
# 틀린 답변, 내일 고민하자

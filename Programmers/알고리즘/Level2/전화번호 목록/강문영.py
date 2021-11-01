# 모범 답안
# import re
#
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1): #O(n)
#         if phone_book[i]<phone_book[i+1]:
#             if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#                 return False
#     else:
#         return True

# 11/1 멍청한 풀이.. 다시 회개하자  무냉공주
def solution(phone_book):
    for idx, num in enumerate(phone_book):
        for cpr_num in phone_book[:idx]+phone_book[idx+1:]:
            if num==cpr_num[:len(num)]:
                return False
    return True
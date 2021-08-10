# import re
#
# result = []
#
# # 예외 처리가 안됨
# # -100*-220
# # [] * 마지막에 이런게 남아버리면 연산이 안됨
# # 아니면 중간에라도 -* 붙어있는 것들 ...
# def extract_order(order=""):
#     if len(order) == 3:
#         result.append(order)
#         return
#
#     if "+" not in order:
#         extract_order(order + "+")
#     if "-" not in order:
#         extract_order(order + "-")
#     if "*" not in order:
#         extract_order(order + "*")
#
# def solution(expression):
#     extract_order()
#     max = -1111
#     for i in result:
#         temp = expression
#         for j in i:
#             if j == "-":
#                 cal_pattern = re.compile("[0-9]+-[0-9]+")
#             else:
#                 cal_pattern = re.compile(f"[0-9]+[{j}][0-9]+")
#             target_exe = cal_pattern.findall(temp)
#             for k in target_exe:
#                 temp = temp.replace(k, str(eval(k)))
#
#         if not temp.isdigit():
#             temp = str(eval(temp))
#
#         if int(abs(int(temp)))>max:
#             max = abs(int(temp))
#
#     return max
#
#
# solution("100-200*300-500+20")


import re

def solution(expression):
    answer = 0
    oper = ["+-*", "+*-", "-*+", "-+*", "*+-", "*-+"]
    for i in range(6):
        check = re.findall("[+*-]+", expression)
        numbers = re.findall("[0-9]+", expression)
        for j in range(3):
            k = 0
            while k < len(check):
                if check[k] == oper[i][j]:
                    numbers[k] = str(eval(numbers[k] + check[k] + numbers[k + 1]))
                    del check[k]
                    del numbers[k + 1]
                else:
                    k += 1
        answer = max(answer, abs(int(numbers[0])))
    return answer

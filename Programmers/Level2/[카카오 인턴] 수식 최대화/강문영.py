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
#                 cal_pattern = re.compile(f"[0-9]+[{{{j}}}][0-9]+")
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
#


from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = (list(permutations(['*','-','+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer
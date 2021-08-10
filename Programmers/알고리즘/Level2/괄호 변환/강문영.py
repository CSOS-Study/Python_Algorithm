def is_balanced_string(s):
    bal = 0
    for p_ in s:
        if p_ == '(':
            bal += 1
        else:
            bal -= 1
    return not (bool(bal))

def is_right_string(s):
    if not is_balanced_string(s):
        return False
    bal = 0
    for s_ in s:
        if s_ == "(":
            bal += 1
        else:
            bal -= 1

        if bal < 0:
            return False

    return True

def convert_balanced_string(s):
    for i in range(2, len(s) + 1, 2):
        if is_balanced_string(s[:i]):
            u, v = s[:i], s[i:]
            break

    if is_right_string(u):
        return u + convert_balanced_string(v)
    else:
        temp = "(" + convert_balanced_string(v) + ")"
        u_ = u.replace("(", ")").replace(")", "(")
        return temp + u_


def solution(p):
    if is_right_string(p):
        return p
    else:
        return convert_balanced_string(p)

# def is_balanced(p):
#     bal = 0
#     for p_ in p:
#         if p_ == '(':
#             bal += 1
#         else:
#             bal -= 1
#     return not (bool(bal))
#
#
# def is_right(p):
#     bal = 0
#     if is_balanced(p) == False:
#         return False
#     for p_ in p:
#         if p_ == '(':
#             bal += 1
#         else:
#             bal -= 1
#         if bal < 0: return False
#     return True
#
#
# def solution(p):
#     if is_right(p) == True:
#         return p
#     for i in range(2, len(p) + 1, 2):
#         if is_balanced(p[:i]) == True:
#             u, v = p[:i], p[i:]
#             break
#     if is_right(u) == True:
#         return u + solution(v)
#     else:
#         result = '(' + solution(v) + ')'
#         for i in u[1:-1]:
#             if i == '(':
#                 result += ')'
#             else:
#                 result += '('
#         return result

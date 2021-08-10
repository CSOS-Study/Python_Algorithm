import re


def confirm_alright(s_list):
    cnt = 0
    for i in s_list:
        if cnt < 0:
            return False
        if i == "(" or i == "{" or i == "[":
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True

    return False

def check(str_list):
    stack = []

    for _str in str_list:
        if _str in ('[', '(', '{'):
            stack.append(_str)
        else:
            if not stack: return False
            x = stack.pop()
            if _str == ']' and x != '[':
                return False
            elif _str == ')' and x != '(':
                return False
            elif _str == '}' and x != '{':
                return False

    if stack: return False
    return True

def solution(s):
    cnt = 0
    for i in range(len(s)):
        u = s[:i]
        v = s[i:]

        if check(v+u):
            cnt +=1
    return cnt

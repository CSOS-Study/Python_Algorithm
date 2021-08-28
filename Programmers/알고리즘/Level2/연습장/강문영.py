import re


def solution(s):
    s_len = len(s)
    result = 11111

    for div_len in range(1, s_len + 1):
        s_list = re.findall(f"[a-z]{{{div_len}}}", s)
        if s_len % div_len != 0:
            s_list.append(s[-(s_len % div_len):])

        stack = []
        cnt = 0

        for idx, element in enumerate(s_list):
            if not stack:
                stack.append(element)
                cnt += 1
            else:
                if stack[-1] == element:
                    cnt += 1
                    if idx == s_len - 1:
                        stack.append(str(cnt) + stack.pop())
                else:
                    if cnt > 1:
                        stack.append(str(cnt) + stack.pop())
                    stack.append(element)
                    cnt = 1

        if len(''.join(stack)) < result:
            result = len(''.join(stack))
            print(''.join(stack))
            print(s_list)
    return result
solution("ababcdcdababcdcd")
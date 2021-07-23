import re

def extract_min(s, n):
    pattern = re.compile(f"[a-z]{{{n}}}")
    stack = pattern.findall(s)
    if len(s) % n != 0:
        stack.append(s[-(len(s) % n):])
    result = []

    cnt = 1
    for i in stack:
        if not result:
            result.append(i)
        elif i == re.sub("[0-9]+", "", result[-1]):
            cnt += 1
            result[-1] = str(cnt) + i
        else:
            result.append(i)
            cnt = 1

    return len(''.join(result))


def solution(s):
    min = 12345
    for i in range(1, len(s) + 1):
        extract_len = extract_min(s, i)
        if min > extract_len:
            min = extract_len

    return min
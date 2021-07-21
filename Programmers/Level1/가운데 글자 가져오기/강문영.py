def solution(s):
    s_len = len(s)
    if len(s) % 2 == 0:
        return s[(s_len // 2) - 1:(s_len // 2) + 1]

    return s[s_len // 2]
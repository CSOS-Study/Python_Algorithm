def solution(s, n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_up = alpha.upper()
    result = ""
    for i in s:
        if i.islower():
            result += alpha[(alpha.index(i)+n)%len(alpha)]
        elif i.isupper():
            result += alpha_up[(alpha_up.index(i)+n)%len(alpha_up)]
        else:
            result += ' '
    return result
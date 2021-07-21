def solution(s):
    upper_s = []
    lower_s = []
    for i in s:
        if i.isupper():
            upper_s.append(i)
        else:
            lower_s.append(i)

    return ''.join(sorted(lower_s, reverse=True)) + ''.join(sorted(upper_s, reverse=True))

# def solution(s):
#     return ''.join(sorted(s, reverse=True))
# 정렬을 반대로 하면 자동으로 대문자는 뒤로 밀려나는군... 몰랐다...

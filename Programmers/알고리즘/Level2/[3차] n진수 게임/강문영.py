def convert_zinbub(num, n):
    result = ""
    while num > 0:
        num, div = divmod(num, n)
        if n > 10 and div >= 10:
            if div == 10:
                result += "A"
            elif div == 11:
                result += "B"
            elif div == 12:
                result += "C"
            elif div == 13:
                result += "D"
            elif div == 14:
                result += "E"
            else:
                result += "F"
        else:
            result += str(div)
    return result[::-1]


def solution(n, t, m, p):
    total = t * m
    answer = []
    result = ""
    for number in range(0, total + 1):
        if number >= 2:
            answer.extend(list(convert_zinbub(number, n)))
        else:
            answer.append(str(number))

    for idx, num in enumerate(answer):
        if len(result) == t:
            break
        if idx % m == p - 1:
            result += num

    return result
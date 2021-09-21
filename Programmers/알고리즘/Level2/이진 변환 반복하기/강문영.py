def convert_binary(s):
    result = ""
    while s > 0:
        s, mod = divmod(s, 2)
        result += str(mod)
    return result[::-1]


def solution(s):
    del_zero = 0
    cnt = 0
    while s != "1":
        cnt += 1
        del_zero += s.count("0")
        s = convert_binary(s.count("1"))

    return [cnt, del_zero]
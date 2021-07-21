def min_num(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def solution(n):
    return sum(min_num(n))
def dfs(n, a, b, cnt):
    if abs(a - b) == 1:
        if a<b and a%2 ==1:
            return cnt
        elif a>b and a%2 ==0:
            return cnt

    a = a // 2 + a % 2
    b = b // 2 + b % 2
    cnt += 1

    return dfs(n, a, b, cnt)


def solution(n, a, b):
    return dfs(n, a, b, 1)

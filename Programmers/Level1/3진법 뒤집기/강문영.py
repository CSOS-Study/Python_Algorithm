# 진법 계산하는 방법을 까먹었다... 나머지를 사용하는 것이었는데
# 왜 까먹었을까...?


def solution(n):
    answer = ''

    while n > 0:
        n, div = divmod(n, 3)
        answer += str(div)

    answer = int(answer, 3)

    return answer

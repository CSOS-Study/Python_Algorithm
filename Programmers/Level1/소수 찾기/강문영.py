# def solution(n):
#     cnt = 0
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             cnt += 1
#
#     return cnt
# 효율성에서 실패함


def solution(n):
    arr = [True] * (n + 1)
    for i in range(2, n + 1):
        if arr[i] == True:
            for j in range(2 * i, n + 1, i):
                arr[j] = False

    return arr[2:].count(True)

## 에라토스 테네스의 체 기억해두자.
# n이 소수가 되려면 2보다 크고 루트 엔보다 작거나 같은 자연수로 나눠 떨어지면 안된다.
# 루트 엔을 표기하는 것
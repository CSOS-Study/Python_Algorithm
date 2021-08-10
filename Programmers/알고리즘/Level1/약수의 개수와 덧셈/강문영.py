def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if counting_divisor(i):
            answer += i
        else:
            answer -= i
    return answer


def counting_divisor(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return True if count % 2 == 0 else False


# 다른 사람 풀이
# 알아둘 팁 : 제곱수는 약수의 개수가 홀수이다.
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
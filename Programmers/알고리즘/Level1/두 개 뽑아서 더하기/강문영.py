from itertools import combinations


def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))

    answer = sorted(list(answer))

    return answer

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))
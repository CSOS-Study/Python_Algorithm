def extract_num(array, command):
    result = array[command[0] - 1:command[1]]
    result.sort()
    return result[command[2] - 1]


def solution(array, commands):
    answer = []

    for i in commands:
        answer.append(extract_num(array, i))

    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])


# 개인적으로 이 풀이는 짧지만, 별로 가독성이 떨어짐 간단한 문제라 이렇게 풀어도 되지만
# 현업에서는 비추
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
# 이 풀이가 좋은 듯
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer
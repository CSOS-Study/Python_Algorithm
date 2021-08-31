# def solution(name):
#     alpha = {
#         "A": 0,
#         "B": 1,
#         "C": 2,
#         "D": 3,
#         "E": 4,
#         "F": 5,
#         "G": 6,
#         "H": 7,
#         "I": 8,
#         "J": 9,
#         "K": 10,
#         "L": 11,
#         "M": 12,
#         "N": 13,
#         "O": 14,
#         "P": 15,
#         "Q": 16,
#         "R": 17,
#         "S": 18,
#         "T": 19,
#         "U": 20,
#         "V": 21,
#         "W": 22,
#         "X": 23,
#         "Y": 24,
#         "Z": 25
#     }
#
#     stack = []
#     for string in name:
#         if not stack:
#             stack.append(alpha[string])
#         else:
#             if stack[-1] > alpha[string]:
#                 stack.append(stack[-1] - alpha[string])
#             else:
#                 stack.append(alpha[string] - stack[-1])
#
#     return sum(stack)
#
# solution("JEROEN")

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer
import re


def calculate_score(dart_score):
    result = []
    score = {
        "S": 1,
        "D": 2,
        "T": 3
    }

    options = {
        "*": 2,
        "#": -1
    }

    for i in range(0, len(dart_score)):
        present_score = dart_score[i]
        if len(present_score) > 2 and present_score[1] != "0":
            if i == 0 or present_score[2] == "#":
                result.append(int(present_score[0]) ** score[present_score[1]] * options[present_score[2]])
            else:
                result.append(result.pop() * 2)
                result.append(int(present_score[0]) ** score[present_score[1]] * 2)
        else:
            if present_score[1] == "0":
                result.append(int(present_score[0:2]) ** score[present_score[2]])
            else:
                result.append(int(present_score[0]) ** score[present_score[1]])
    return sum(result)


def solution(dartResult):
    p = re.compile('[0-9]{1}0?[A-Z]{1}[*#]?')
    result = p.findall(dartResult)

    return calculate_score(result)

# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
#
#     answer = sum(dart)
#     return answer
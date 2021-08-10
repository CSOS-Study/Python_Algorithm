def solution(answers):
    math_giveup1 = [1, 2, 3, 4, 5]
    math_giveup2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_giveup3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = {1: 0, 2: 0, 3: 0}

    for idx, val in enumerate(answers):
        if answers[idx] == math_giveup1[idx % 5]:
            result[1] += 1
        if answers[idx] == math_giveup2[idx % 8]:
            result[2] += 1
        if answers[idx] == math_giveup3[idx % 10]:
            result[3] += 1

    answer = [k for k, v in result.items() if max(result.values()) == v]
    return answer
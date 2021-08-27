def is_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def solution(scores):
    scores = list(map(list, zip(*scores)))
    result = []

    for idx, score in enumerate(scores):
        if (score[idx] == max(score) and score.count(score[idx]) == 1) or (
                score[idx] == min(score) and score.count(score[idx]) == 1):
            temp = (sum(score[:idx]) + sum(score[idx + 1:])) / (len(score) - 1)
        else:
            temp = (sum(score)) / len(score)

        result.append(is_grade(temp))

    return "".join(result)
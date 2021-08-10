def extract_failure(level, stages):
    fail_person = [i for i in stages if i == level]
    total_person = [j for j in stages if j >= level]

    if len(total_person) == 0:
        return 0
    return len(fail_person) / len(total_person)


def solution(N, stages):
    result = {}

    for i in range(1, N + 1):
        result[i] = extract_failure(i, stages)

    sort_result = [i[0] for i in sorted(result.items(), key=lambda x: x[1], reverse=True)]

    return sort_result
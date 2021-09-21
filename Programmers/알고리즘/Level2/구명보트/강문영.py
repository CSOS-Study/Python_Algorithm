def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    cnt = 0

    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return cnt
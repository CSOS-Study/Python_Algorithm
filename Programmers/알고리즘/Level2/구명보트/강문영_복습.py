# def solution(people, limit):
#     people.sort()
#     p = 0
#     q = len(people) - 1
#     cnt = 0
#
#     while p <= q:
#         if people[p] + people[q] <= limit:
#             cnt += 1
#             p += 1
#             q -= 1
#         else:
#             cnt += 1
#             q -= 1
#
#     return cnt

def solution(people, limit):
    people.sort()
    p = 0
    q = len(people) - 1
    cnt = 0

    while p <= q:
        if people[p] + people[q] <= limit:
            cnt += 1
            p += 1
        q -= 1

    return cnt
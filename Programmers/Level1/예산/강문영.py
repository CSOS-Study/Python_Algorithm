# 정렬을 하면 된다는 것을....
# 일단 정렬을 하고 보자.. greedy계열은 말이다...
# 가장많이 ~ 할 수 있는? -> 그리디..
# def solution(d, budget):
#     d.sort()
#     result = 0
#     for i in d:
#         if result + i > budget:
#             return d.index(i)
#         else:
#             result += i
#
#     return len(d)

def solution(d, budget):
    d.sort()
    result = 0
    count =0
    for i in d:
        if result + i >budget:
            return count
        else:
            result += i
            count +=1
    else:
        return len(d)
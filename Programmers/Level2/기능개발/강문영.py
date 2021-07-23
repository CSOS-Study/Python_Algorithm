import math


def solution(progresses, speeds):
    needs_day = []
    for i in range(0, len(progresses)):
        needs_day.append(math.ceil((100 - progresses[i]) / speeds[i]))

    answer = []
    result = []
    cnt = 1
    ## 달라질때만 이전에 cnt를 넣어준다.
    ## 달라지지 않으면? cnt 넣는게 없음
    ## 달라져도 지금의 cnt는 넣지 않는다. 따라서 마지막에 처리를 해줘야함
    for i in needs_day:
        if not answer:
            answer.append(i)
        elif answer[-1] >= i:
            cnt += 1
        else:
            result.append(cnt)
            answer.append(i)
            cnt = 1

    result.append(cnt)

    return result
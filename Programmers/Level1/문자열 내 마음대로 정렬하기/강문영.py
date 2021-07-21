def solution(strings, n):
    alpha = {}
    for i in strings:
        alpha[i] = i[n]

    sorted_value = sorted(alpha.items(), key=lambda x: (x[1], x[0]))
    ## 다중 정렬 조건 알아두기 람다는 굿이다!!
    ## 람다에 대해서 정리해두기
    return [i[0] for i in sorted_value]
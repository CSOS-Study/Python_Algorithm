def solution(n):
    if n<4:
        return ["1","2","4"][n%3-1 if n<3 else 2]
    if n%3==0:
        n = n-3
    return str(solution(n//3))+str(solution(n%3))
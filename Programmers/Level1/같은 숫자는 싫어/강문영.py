def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
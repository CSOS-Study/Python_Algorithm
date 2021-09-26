def solution(s):
    cnt =0
    for str in s:
        if cnt <0:
            return False
        if str == "(":
            cnt +=1
        else:
            cnt -=1
    if cnt !=0:
        return False
    return True
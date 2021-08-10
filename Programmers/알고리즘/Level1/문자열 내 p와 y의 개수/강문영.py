def solution(s):
    s = s.lower()
    cnt_y = 0
    cnt_p =0
    for i in s:
        if i == "y":
            cnt_y +=1
        if i == "p":
            cnt_p +=1

    return True if cnt_y==cnt_p or (cnt_y ==0 and cnt_p ==0) else False
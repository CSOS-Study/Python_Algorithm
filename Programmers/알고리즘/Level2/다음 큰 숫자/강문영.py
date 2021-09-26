def solution(n):
    str_ = bin(n)[2:]
    cnt = str_.count("1")
    max = int("1"+str_,2)
    # 다음 1이 추가된 것 까지만 확인하기
    for num in range(n+1, max):
        temp = bin(num)[2:]
        if temp.count("1") == cnt:
            return int(temp,2)
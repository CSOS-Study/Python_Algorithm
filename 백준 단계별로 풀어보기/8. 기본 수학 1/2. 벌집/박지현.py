"""
1개를 지나는 것 : 1
2개를 지나는 것 : 2~7 //6개
3개를 지나는 것 : 8~19 //12개
4개를 지나는 것 : 20~37 //18개
5개를 지나는 것 : 38~61 //24개
6개를 지나는 것 : 62~93 //32개
규칙 : 6개씩 개수가 늘어남
"""

N,num,i = int(input()), 1, 1
if N==num:print(num)
else:
    while True:
        if N <= num+(6*i):
            print(i+1)
            break
        else:
            num+=(6*i)
            i+=1
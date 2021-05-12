N, cnt =int(input()), 0
zong_num = 666 # 기준 넘버 : 이걸 계속 +1씩 증가하면서 종말 숫자를 찾는다

while True:
    if '666' in str(zong_num):
        cnt+=1
    if cnt == N :
        print(zong_num)
        break
    zong_num+=1 #모든 경우의 수를 모두 탐색하는 것
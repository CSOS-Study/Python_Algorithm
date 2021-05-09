'''
입력받은 좌표 값들 중,
중복되지 않는 x값, 중복되지 않는 y값으로 좌표를 이루면
마지막 좌표가 됨
'''
x_lst=[]
y_lst=[]
for _ in range(3):
    x,y=map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
for i in range(3):
    if x_lst.count(x_lst[i]) == 1: final_x = x_lst[i]
    if y_lst.count(y_lst[i]) == 1: final_y = y_lst[i]

print(final_x,final_y)
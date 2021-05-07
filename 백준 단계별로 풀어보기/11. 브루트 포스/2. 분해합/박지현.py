'''
생성자 문제
M의 분해합으로 N이 만들어질 때, 이때의 M을 '생성자'라고 함.
N의 생성자 M을 찾아라.
'''
N,sum_lst = int(input()), []

for num in range(1,N+1):
    lst = list(str(num))
    summ = num + sum(map(int,lst)) # num=216일 때, 216+(2 + 1 + 6) 하는 과정
    if summ == N : sum_lst.append(num)

if len(sum_lst)==0:print(0)
else:print(min(sum_lst))
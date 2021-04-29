number1,number2 = map(int,input().split())

n_list = [0 for _ in range(0, number2+1)]
n_list[0:2] = [1,1]
for i in range(2, number2+1):
    if n_list[i] == 0:
        j = 2
        while i * j <= number2:
            n_list[i * j] = 1
            j += 1

for i, value in enumerate(n_list):
    if value == 0 and i >=number1:
        print(i)

number1 = int(input())
number2 = int(input())

n_list = [0 for _ in range(0, number2+1)]
n_list[0:2] = [1,1]
for i in range(2, number2+1):
    if n_list[i] == 0:
        j = 2
        while i * j <= number2:
            n_list[i * j] = 1
            j += 1

res_list = [i for i, value in enumerate(n_list) if value == 0 and i >=number1]
if len(res_list)>0:
    print(sum(res_list))
    print(res_list[0])
else:
    print(-1)

n_list = list(map(int, input().split()))
for i in range(0,2):
    result = 0
    while n_list[i]!=0:
        result = result*10 + n_list[i]%10
        n_list[i] = n_list[i]//10
    n_list[i] = result

print(n_list[0] if n_list[0]>n_list[1] else n_list[1])


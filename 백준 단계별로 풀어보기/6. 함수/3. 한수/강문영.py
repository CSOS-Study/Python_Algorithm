def is_han_num(num):
    number_list = list(map(int,str(num)))
    if number_list[2] - number_list[1] == number_list[1] - number_list[0]:
        return 1
    return 0

n = int(input())
result =0
for i in range(1,n+1):
    if i>=100:
        result += is_han_num(i)
    else:
        result +=1
#         1,2,.. 9
# 10, 11, 12, ... 99
print(result)
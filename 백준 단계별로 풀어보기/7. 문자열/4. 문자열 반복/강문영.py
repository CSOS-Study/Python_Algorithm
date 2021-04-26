t = int(input())
result_string =''
for _ in range(0,t):
    repeat_num,target_string = input().split()
    for i in str(target_string):
        result_string += i*int(repeat_num)
    result_string +='\n'
print(result_string)
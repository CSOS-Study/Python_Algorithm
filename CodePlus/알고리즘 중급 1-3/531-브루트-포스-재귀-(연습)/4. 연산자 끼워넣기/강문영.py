from itertools import permutations
n = int(input())
n_list = list(map(int,input().split()))
calculate_list = list(map(int,input().split()))
calculate_result = ['+','-','*','%']

for idx,val in enumerate(calculate_list):
    calculate_result[idx] = calculate_result[idx]*val

calculate_result = list(''.join(calculate_result))

def is_pass(cal_list):
    result = n_list[0]
    idx = 0
    while idx<len(cal_list):
        if cal_list[idx] == '+':
            result = result + n_list[idx+1]
        elif cal_list[idx] == '-':
            result = result - n_list[idx+1]
        elif cal_list[idx] == '*':
            result = result * n_list[idx+1]
        else:
            if result<0:
                result = result * -1
                result = result //n_list[idx+1]
                result = result * -1
            else:
                result = result // n_list[idx+1]
        idx +=1
    return result

result_list = []

for i in set(permutations(calculate_result)):
    result_list.append(is_pass(i))

print(max(result_list))
print(min(result_list))
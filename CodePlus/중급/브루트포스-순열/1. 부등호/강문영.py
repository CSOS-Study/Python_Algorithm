from itertools import permutations
n = int(input())
up_and_down_list = list((input().split()))


def is_right_case(number_list):
    for idx, val in enumerate(up_and_down_list):
        if val == '<':
            if number_list[idx] >= number_list[idx + 1]:
                break
        else:
            if number_list[idx] <= number_list[idx + 1]:
                break
    else:
        return True
    return False

result_list =[]

for i in list(permutations(range(0,10),n+1)):
    if is_right_case(list(i)):
        result_list.append(list(map(str,i)))

print(''.join(result_list))
print(''.join(min(result_list)))
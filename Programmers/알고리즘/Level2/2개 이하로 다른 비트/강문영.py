# def extract_min(num):
#     cnt = 1
#     while True:
#         cpr_num = format(num+cnt,'b')
#         real_num = format(num,'b')[::-1]
#         is_equal = 0

#         real_num += "0"*(len(cpr_num)-len(real_num))
#         real_num = real_num[::-1]

#         for i in range(len(real_num)):
#             if is_equal>2:
#                 break
#             if cpr_num[i] != real_num[i]:
#                 is_equal+=1

#         if is_equal<=2:
#             return num+cnt
#         cnt +=1


# def solution(numbers):
#     result = []
#     for num in numbers:
#         result.append(extract_min(num))
#     return result

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer
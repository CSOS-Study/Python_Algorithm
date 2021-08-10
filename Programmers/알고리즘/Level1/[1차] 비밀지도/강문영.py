def extract_binary(arr, n):
    result = []
    for i in arr:
        temp = ''
        while i > 0:
            i, res = divmod(i, 2)
            temp += str(res)
        if len(temp) < n:
            temp += '0' * (n - len(temp))

        result.append(temp[::-1])

    return result


def solution(n, arr1, arr2):
    answer = []
    binary1 = extract_binary(arr1, n)
    binary2 = extract_binary(arr2, n)

    for b1, b2 in zip(binary1, binary2):
        b1_int = list(b1)
        b2_int = list(b2)

        for i in range(0, n):
            if b1_int[i] == b2_int[i] and b1_int[i] == '0':
                b1_int[i] = ' '
            else:
                b1_int[i] = '#'

        answer.append(''.join(b1_int))

    return answer


# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer
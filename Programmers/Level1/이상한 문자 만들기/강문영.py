def solution(s):
    s_list = s.split(" ")
    result = []
    for i in s_list:
        temp = ''
        for j in range(0, len(i)):
            if j % 2 == 0:
                temp += i[j].upper()
            else:
                temp += i[j].lower()
        result.append(temp)

    return ' '.join(result)

# split이 좀 그랬다.
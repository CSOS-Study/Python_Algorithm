def solution(msg):
    dic = dict()
    lst = []
    [lst.append(chr(i)) for i in range(ord('A'), ord('Z') + 1)]
    for idx, char in enumerate(lst):
        dic[char] = idx + 1
    idx = 0
    maxIdx = 26
    length = 0
    answer = []

    while True:
        length += 1
        if msg[idx:idx + length] not in dic.keys():
            answer.append(dic[msg[idx:idx + length - 1]])
            maxIdx += 1
            dic[msg[idx:idx + length]] = maxIdx
            idx = idx + length - 1
            length = 0
        else:
            if idx + length - 1 == len(msg):
                answer.append(dic[msg[idx:idx + length]])
                break

    return answer
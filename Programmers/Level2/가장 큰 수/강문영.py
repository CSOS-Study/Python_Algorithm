def solution(num):
    num_list = list(map(str,num))
    num_list.sort(key=lambda x:x*3, reverse= True)
    return ''.join(num_list)
import collections


def solution(record):
    result = []
    user_list = collections.defaultdict(list)

    for i in record:
        temp = i.split()
        if len(temp) > 2:
            user_list[temp[1]].append(temp[2])

    for i in record:
        temp = i.split()
        if "Enter" == temp[0]:
            result.append(f"{user_list[temp[1]][-1]}님이 들어왔습니다.")
        if "Leave" == temp[0]:
            result.append(f"{user_list[temp[1]][-1]}님이 나갔습니다.")

    return result

# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]
#
#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
#
#     return answer
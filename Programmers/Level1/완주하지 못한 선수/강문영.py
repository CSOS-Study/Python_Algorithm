import collections


def solution(participant, completion):
    patici_dict = collections.Counter(participant)
    comple_dict = collections.Counter(completion)

    for i in patici_dict.keys():
        if patici_dict[i] != comple_dict[i]:
            return i


# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
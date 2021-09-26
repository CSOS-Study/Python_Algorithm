import re

head = re.compile("[a-zA-Z-]+")
number = re.compile("[0-9]+")


def joining(str):
    str = ''.join(str)
    return str


def solution(files):
    file_dict = [re.split(r"([0-9]+)", s) for s in files]
    file_list = sorted(file_dict, key=lambda x: (x[0].lower(), int(x[1])))
    file_list = list(map(joining, file_list))

    return file_list


import re

head = re.compile("[a-zA-Z- .]+")
number = re.compile("[0-9]+")


def joining(str):
    str = ''.join(str)
    return str


def solution(files):
    # file_dict = [re.split(r"([0-9]+)", s) for s in files]
    # print(file_dict)
    file_dict = []

    for file in files:
        head_str = head.match(file).group()
        number_str = number.search(file).group()
        tail = file[number.search(file).end():]
        file_dict.append((head_str, number_str, tail))

    print(file_dict)
    file_list = sorted(file_dict, key=lambda x: (x[0].lower(), int(x[1])))
    file_list = list(map(joining, file_list))

    return file_list
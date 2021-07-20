def solution(s):
    mapping_table = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for i in mapping_table.keys():
        s = s.replace(i, str(mapping_table[i]), len(s))

    return int(s)
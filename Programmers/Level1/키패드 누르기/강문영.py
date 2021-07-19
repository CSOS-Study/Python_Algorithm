import math


def distance_list(list1, list2):
    x = list1[0] - list2[0]
    y = list1[1] - list2[1]
    # distance = math.sqrt((x * x) + (y * y))
    distance = abs(x) + abs(y)
    return distance


def solution(numbers, hand):
    keypad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2]
    }

    right = "#"
    left = "*"

    left_list = [1, 4, 7]
    right_list = [3, 6, 9]
    result = []

    for i in numbers:
        now_point = i
        if now_point in left_list:
            result.append("L")
            left = now_point
        elif now_point in right_list:
            result.append("R")
            right = now_point
        else:
            right_distance = distance_list(keypad.get(right), keypad.get(now_point))
            left_distance = distance_list(keypad.get(left), keypad.get(now_point))
            if right_distance < left_distance:
                result.append("R")
                right = now_point
            elif right_distance > left_distance:
                result.append("L")
                left = now_point
            else:
                if hand == "right":
                    result.append("R")
                    right = now_point
                else:
                    result.append("L")
                    left = now_point

    return ''.join(result)

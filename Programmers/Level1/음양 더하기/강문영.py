def solution(absolutes, signs):
    result = 0
    for idx, val in enumerate(absolutes):
        if signs[idx]:
            result = result + val
        else:
            result = result - val

    return result


#
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
def solution(x):
    hasha = sum(map(int, str(x)))

    if x % hasha == 0:
        return True
    return False
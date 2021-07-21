import re


def solution(s):
    pattern = re.compile("^[0-9]{4}$|^[0-9]{6}$")

    return True if pattern.match(s) else False
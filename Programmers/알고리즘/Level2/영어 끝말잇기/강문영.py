from collections import defaultdict


def solution(n, words):
    result = 0
    stack = []
    for idx, word in enumerate(words):
        if not stack:
            stack.append(word)
        else:
            if word in stack or stack[-1][-1] != word[0]:
                result = idx + 1
                break
            else:
                stack.append(word)
    else:
        return [0, 0]

    if result % n == 0:
        return [n, result // n]

    return [result % n, result // n + 1]
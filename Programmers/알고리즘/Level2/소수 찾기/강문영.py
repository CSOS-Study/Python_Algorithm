from itertools import permutations

prime = [True] * (10000001)


def eratostenes():
    prime[0] = prime[1] = False
    for i in range(2, 10000001):
        if prime[i] == True:
            for j in range(2 * i, 10000001, i):
                prime[j] = False


def solution(numbers):
    eratostenes()
    num_card = list(numbers)
    pick_num = set()
    cnt = 0

    for N in range(1, len(numbers) + 1):
        permutate_num = permutations(num_card, N)
        for i in permutate_num:
            pick_num.add(int(''.join(i)))

    for k in pick_num:
        if prime[k]:
            cnt += 1

    return cnt
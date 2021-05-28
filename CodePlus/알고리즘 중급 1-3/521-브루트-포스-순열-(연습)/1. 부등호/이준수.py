from itertools import permutations

def solve(number):
    for i in permutations(number, N+1):
        for idx in range(1, N+1):
            if sign[idx - 1] == '<' and i[idx - 1] > i[idx]:
                break
            elif sign[idx - 1] == '>' and i[idx - 1] < i[idx]:
                break
        else:
            return print(''.join(i))


N = int(input())
sign = input().split()
number = "0123456789"
solve(number[::-1])
solve(number)
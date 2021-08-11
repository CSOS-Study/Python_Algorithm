# idx를 뽑거나 뽑지 않는 경우의수.
# idx 현재 판단의 기준이되는 idx / 누적합 acc
'''

'''
def partial_sequence(idx: int, acc: int):
    if idx == len(sequence):
        return 1 if acc == S else 0
    return partial_sequence(idx + 1, acc + sequence[idx]) + partial_sequence(idx + 1, acc)


N, S = map(int, input().split())
sequence = list(map(int, input().split()))
res = partial_sequence(0, 0)
print(res - 1 if S == 0 else res)
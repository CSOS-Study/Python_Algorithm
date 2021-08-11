N = int(input())
S = list(map(int, input().split()))
num_set = set(range(1,20*100000+1))
for i in range(1<<N):
    part_sum = 0
    for j in range(N):
        if i & 1 << j:
            part_sum += S[j]
    num_set.discard(part_sum)
print(min(num_set))
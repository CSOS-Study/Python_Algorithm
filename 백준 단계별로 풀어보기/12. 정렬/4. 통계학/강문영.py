import sys
import collections
n = int(input())
n_list = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

print(round(sum(n_list)/n))
print(n_list[n//2])
counts = collections.Counter(n_list).most_common(2)
print(counts[-1][0] if counts[0][1] == counts[-1][1] else counts[0][0])
print(n_list[-1]- n_list[0])
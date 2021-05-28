import collections
import sys

N = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(N)]
dict = collections.defaultdict(int)

for word in words:
    for idx, w in enumerate(word[::-1]):
        dict[w] = dict[w] + 10 ** idx

nums = sorted(dict.values(), reverse=True)
res = 0

for idx, num in enumerate(nums):
    res += num * (9-idx)

print(res)

#string배열을 set으로 하는 방법
#dict value를 기준으로 정렬
#가중치
# 중복이 몇개든말든 가장 높은 자리수의 알파벳이 가장 큰 값을 가져야 한다.
import sys
from collections import defaultdict

n = int(input())
word = []
for _ in range(n):
    word.append(list(sys.stdin.readline()[:-1][::-1]))

dic = defaultdict(int)
for i in word:
    level = 1
    for j in i:
        dic[j] += level
        level *= 10

total, i = 0, 9
for k, v in sorted(dic.items(), reverse=True, key=lambda x: x[1]):
    total += v * i
    i -= 1
print(total)
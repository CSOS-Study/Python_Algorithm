import sys

N = int(input())
words = set(sys.stdin.readline().rstrip() for _ in range(N))
for word in sorted(words, key=lambda w:(len(w), w)):
    print(word)
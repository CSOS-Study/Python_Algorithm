import sys

case=set(sys.stdin.readline() for _ in range(int(input())))
print(''.join(sorted(case, key=lambda x:(len(x),x))))
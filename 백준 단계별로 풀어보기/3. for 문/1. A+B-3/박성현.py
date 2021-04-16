import sys

# 1번
i = int(input())
for j in range(1,10):
    print(i, '*', j, '=', i * j)

# 2번
for i in range(int(input())):
    print(sum(map(int, input().split())))

# 3번
print(sum(range(int(input())+1)))

# 4번
for _ in range(int(input())):
    print(sum(map(int, sys.stdin.readline().split())))

# 5번
for i in range(int(input())):
    print(i+1)

# 6번
for i in range(int(input()), 0, -1):
    print(i)

# 7번
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i+1) + ": " + str(a + b))

# 8번
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i+1) + ":", a, '+', b, '=', a + b)

# 9번
for i in range(1, int(input())+1):
    print('*' * i)

# 10번
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)

# 11번
n, x = map(int, input().split())
a = ''
for i in list(map(int, input().split())):
    if i < x: a += str(i)+' '
print(a.rstrip())
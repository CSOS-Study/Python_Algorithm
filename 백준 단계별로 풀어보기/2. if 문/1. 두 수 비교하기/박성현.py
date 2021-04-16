# 1번
a, b = map(int, input().split())
print('<' if a < b else '==' if a == b else '>')

# 2번
n = int(input())
print('A' if n > 89 else 'B' if n > 79 else 'C' if n > 69 else 'D' if n > 59 else 'F')

# 3번
n = int(input())
print(1 if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else 0)

# 4번
a = int(input())
b = int(input())
print(1 if a>0 and b>0 else 2 if a<0 and b>0 else 3 if a<0 and b<0 else 4)

# 5번
a, b = map(int, input().split())
if b >= 45:
    print(a, b-45)
elif a == 0:
    print(23, 15+b)
else:
    print(a-1, 15+b)
a, b = map(int, input().strip().split(' '))
result = ''
for _ in range(b):
    result += "*" * a
    result += '\n'

print(result)
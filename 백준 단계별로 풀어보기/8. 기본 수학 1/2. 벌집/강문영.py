n = int(input())
deadline = 1
i = 1
while n > deadline:
    deadline += 6 * i
    i += 1

print(i)

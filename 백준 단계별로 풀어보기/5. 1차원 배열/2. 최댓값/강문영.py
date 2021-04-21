max = 1
index = 0
for i in range(0,9):
    temp = int(input())
    if max<temp:
        max = temp
        index = i+1

print(max)
print(index)

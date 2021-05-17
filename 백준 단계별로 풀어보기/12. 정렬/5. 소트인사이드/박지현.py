num = list(input())
num = [int(i) for i in num]
for i in sorted(num,reverse=True): print(i, end='')
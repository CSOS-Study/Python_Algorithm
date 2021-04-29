n= int(input())
case = list(map(int, input().split()))
for i in case:
    if i==1: n -= 1
    for j in range(2, int(i**0.5)+1):
        if not i%j:
            n -= 1
            break
print(n)
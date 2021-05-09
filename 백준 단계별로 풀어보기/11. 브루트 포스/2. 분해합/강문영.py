n = int(input())
def product_num(n):
    result = n
    while n !=0:
        result += n%10
        n = n//10
    return result

for i in range(n):
    if n == product_num(i):
        print(i)
        break
else:
    print(0)

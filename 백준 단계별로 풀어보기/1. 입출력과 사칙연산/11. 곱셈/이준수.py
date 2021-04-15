a = int(input())
b = int(input())
b_ = b
while(b_):
    print(a * (b_ % 10))
    b_ //= 10
print(a*b)
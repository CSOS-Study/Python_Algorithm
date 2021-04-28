a, b = input().split()
a_r=int(a[::-1])
b_r=int(b[::-1])
print(a_r) if a_r>b_r else print(b_r)
x = int(input())

start_idx = 1
r = 1

while start_idx + r <= x:
    start_idx += r
    r += 1

a = 1
b = r
while start_idx != x:
    a += 1
    b -= 1
    start_idx += 1

if r % 2:
    a, b = b, a
print("{}/{}".format(a, b))

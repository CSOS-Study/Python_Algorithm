import string

dial = {}
c, id, ans = 1, 0, 0
for i in [3, 3, 3, 3, 3, 4, 3, 4]:
    c += 1
    for j in string.ascii_uppercase[id:id+i]:
        dial[j] = c
    id += i
for i in str(input()):
    ans += dial[i] + 1
print(ans)

import string

s, ans = str(input()), ''
for i in string.ascii_lowercase:
    if i in s: ans += str(s.index(i)) + ' '
    else: ans += '-1 '
print(ans)

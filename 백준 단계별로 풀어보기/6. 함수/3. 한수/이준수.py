res = n = int(input())
if(n > 99):
    res = 99
    for i in range(100,n+1):
        s = str(i)
        if(int(s[0])-int(s[1]) == int(s[1]) - int(s[2])):
            res += 1
print(res)
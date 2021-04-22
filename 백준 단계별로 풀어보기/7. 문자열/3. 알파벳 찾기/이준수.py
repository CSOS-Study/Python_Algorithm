l = [-1]*26
s = [ord(i)-ord('a') for i in input()]
for idx, val in enumerate(s):
    if(l[val]==-1):
        l[val] = idx
for i in l:
    print(i,end=' ')
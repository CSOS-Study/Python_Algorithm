s = input()
d = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in d:
    s = s.replace(i,'!')
print(len(s))
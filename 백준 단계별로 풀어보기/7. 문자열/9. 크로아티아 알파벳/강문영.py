l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in range(len(l)):
    s = s.replace(l[i], '1')
print(len(s))
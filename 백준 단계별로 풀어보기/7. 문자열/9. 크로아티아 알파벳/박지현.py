word = input()
cro_lst =['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro_lst:
    word = word.replace(i,'a')
print(len(word))
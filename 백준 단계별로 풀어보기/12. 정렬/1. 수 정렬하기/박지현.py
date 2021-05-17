lst=[]
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort()
for i in lst: print(i)

'''
# 버블 정렬
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:
            lst[i], lst[j]= lst[j],lst[i]
print(lst)
'''
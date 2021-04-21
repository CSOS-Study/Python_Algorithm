def d(n):
    num = n
    for x in list(str(n)):
        num += int(x)
    return num # 생성자가 있는 값만 return 됨

y=[]
for i in range(1,10001):
    y.append(d(i))

for i in range(1,10001):
    if i in y:
        pass
    else:
        print(i) # 셀프넘버
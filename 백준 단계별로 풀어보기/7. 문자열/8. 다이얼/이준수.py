dial_number = {"ABC":2,"DEF":3,"GHI":4,"JKL":5,"MNO":6,"PQRS":7,"TUV":8,"WXYZ":9}
result = 0
for i in input():
    for dial in dial_number.keys():
        if i in dial:
            result += dial_number[dial] +1
            break
print(result)
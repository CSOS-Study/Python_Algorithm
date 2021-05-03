left, right = [], []
for _ in range(3):
    x, y = map(int, input().split())
    if x in left: left.remove(x)
    else: left.append(x)    
    if y in right: right.remove(y)
    else: right.append(y)   
print(left[0], right[0])
a = []
while True:
    try:
        a.append(int(input()))
    except EOFError:
        break
print(max(a))
print(a.index(max(a))+1)
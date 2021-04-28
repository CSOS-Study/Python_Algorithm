i = int(input())
if i == 1 :
    print(i)
else :
    j = 1
    while not(3*j*j - 3*j + 2 <= i and i <= 3*j*j+3*j+1):
        j+=1
    print(j+1)
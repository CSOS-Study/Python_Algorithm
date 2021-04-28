n = int(input())

def find_number(n):
    i = 1
    while True:
        if sum(range(i+1)) >= n:
            break
        i +=1
    return i

idx = find_number(n)
num_loop = n - sum(range(idx))

if idx%2 == 0:
    print(str(num_loop) + '/'+ str((idx-num_loop)+1))
else:
    print(str((idx-num_loop)+1)+'/'+str(num_loop))

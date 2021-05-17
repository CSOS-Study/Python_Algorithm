from itertools import permutations

N = int(input())
sign = input().split()
number = list(map(int, range(10)))
res = []

for i in permutations(number, N+1):
    flag = False
    for idx in range(1,N+1):
        if sign[idx-1] == '<' and i[idx-1] > i[idx]:
            break

        if sign[idx-1] == '>' and i[idx-1] < i[idx]:
            break
    else:
        flag = True
    if flag:
        res.append(i)

print(''.join(map(str,res[-1])))
print(''.join(map(str,res[0])))
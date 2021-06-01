import itertools, sys

def search(tup):
    for i in range(len(sign)):
        if sign[i] == '>' and tup[i] < tup[i+1]:
            return False
        if sign[i] == '<' and tup[i] > tup[i+1]:
            return False
    return True

k = int(sys.stdin.readline())
sign = list(sys.stdin.readline().split())
lst = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9],k+1)) #순열

for i in reversed(lst): # 가장 먼저 True로 판명난게 최댓값
    if search(i):
        print(''.join(list(map(str,i))))
        break
for i in lst: # 가장 먼저 True로 판명난게 최솟값
    if search(i):
        print(''.join(list(map(str,i))))
        break
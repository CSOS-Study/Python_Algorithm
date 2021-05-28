'''
N = int(input())
S = list(map(int, input().split()))
num_set = set(range(1,20*100000+1))
for i in range(1<<N):
    part_sum = 0
    for j in range(N):
        if i & 1 << j:
            part_sum += S[j]
    num_set.discard(part_sum)
print(min(num_set))


n=int(input())
a=sorted(map(int,input().split()))
s=0
for x in a:
  if s+1<x:
    print(s+1)
    exit()
  s+=x
print(s+1)
'''

N = int(input())
S = list(map(int,input().split()))
part_sum = {0}
for x in S:
    part_sum |= {y+x for y in part_sum}
for res in range(100000*20+1):
    if res not in part_sum:
        print(res)
        break
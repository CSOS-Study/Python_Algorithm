import sys
from collections import defaultdict

n = int(sys.stdin.readline())
lst = []
#역순으로 저장한다.
for _ in range(n):
    lst.append(list(sys.stdin.readline()[:-1][::-1]))

dic=defaultdict(int) #디폴트 dict 생성
for i in lst:
    cnt=1 #우선순위를 의미 (cnt가 클수록 우선순위가 높음)
    for j in i:
        dic[j] += cnt
        cnt*=10

num, total = 9, 0
sort_dic = sorted(dic.items(), reverse=True, key = lambda x:x[1])
for i in sort_dic:
    total += i[1]*num #우선순위가 큰것부터 큰수(9~)를 곱해서 더한다.
    num-=1

print(total)
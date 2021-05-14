import sys
from collections import Counter

cnt_lst=[]
for i in range(int(sys.stdin.readline())):
    cnt_lst.append(int(sys.stdin.readline()))
cnt_lst.sort()
cnt_dic = Counter(cnt_lst).most_common(2)

print(round(sum(cnt_lst)/len(cnt_lst))) #산술평균
print(cnt_lst[int(len(cnt_lst)//2)]) #중앙값
if len(cnt_dic)>1:
    if cnt_dic[0][1]==cnt_dic[1][1]: print(cnt_dic[1][0]) #최빈값
    else: print(cnt_dic[0][0])
else: print(cnt_dic[0][0])
print(cnt_lst[-1]-cnt_lst[0]) #범위
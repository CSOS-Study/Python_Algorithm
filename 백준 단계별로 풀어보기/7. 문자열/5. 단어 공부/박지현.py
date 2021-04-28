alpha, lst, dup, dic = input().upper(), [], 0, {}

for i in set(alpha): # 중복 제거한 알파벳만 검색
    lst.append(alpha.count(i)) # 각 알파벳 개수 저장
    dic[i] = alpha.count(i) # 각 알파벳과 개수 함께 저장

for inx, cnt in enumerate(lst): # 튜플로 접근
    if cnt == max(lst):
        dup+=1

if dup>1: print('?')
else: print(max(dic,key=dic.get)) #max(key=.get) : max value의 key값 도출
n=int(input())
case=list(map(int, input().split()))
set_case=sorted(set(case))
dic={set_case[i]:i for i in range(len(set_case))}
for i in case:
    print(dic[i],end=' ')
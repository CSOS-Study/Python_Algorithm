'''
+A -B(하루)가 반복되며, 마지막엔 +A만 한다.
V높이 까지 올라가는데 몇일이 걸릴까?

어차피 마지막엔 +A를 하니까, V-A 만큼을 +A -B(하루)로 몇번 반복해서 올라가는지
즉, 몇일 걸려서 V-A까지 올라가는지 찾고, +1(마지막 하루에 +A 올라가는거 더하기)
'''
import math

A,B,V = map(int,input().split())
if A>=V: print(1)
else: print(math.ceil((V-A)/(A-B)+1))

''''
# Bad case : 시간 초과
A,B,V = map(int,input().split())
total_l, cycle = 0, 1
while True:
    total_l+=A
    if total_l >= V:
        print(cycle)
        break
    total_l-=B
    cycle+=1
'''
m, n, case = int(input()), int(input()), []
for i in range(m, n+1):
    if i==1: continue
    chk = True
    for j in range(2, int(i**0.5)+1):
        if not i%j:
            chk = False
    if chk:
        case.append(i)
if not case: print(-1)
else: print('{}\n{}'.format(sum(case), min(case)))
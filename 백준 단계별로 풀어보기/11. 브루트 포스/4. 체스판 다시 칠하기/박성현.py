n,m=map(int, input().split())
g=[input() for _ in range(n)]
res=[]
for a in range(n-7):
    for b in range(m-7):
        black,white=0,0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2:
                    if g[i][j]!='B':
                        black+=1
                    if g[i][j]!='W':
                        white+=1
                else:
                    if g[i][j]!='W':
                        black+=1
                    if g[i][j]!='B':
                        white+=1
        res.extend([black,white])
print(min(res))
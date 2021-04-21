N=int(input())
H=0
for i in range(1,N+1):
    if i<=99: #99이하는 모두 한수
        H+=1
    else:
        N_H=list(str(i))
        if int(N_H[0])-int(N_H[1])==int(N_H[1])-int(N_H[2]):
            H+=1
print(H)
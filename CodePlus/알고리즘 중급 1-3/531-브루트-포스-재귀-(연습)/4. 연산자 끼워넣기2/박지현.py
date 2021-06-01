'''
DFS개념 (트리 그리면서 풀기)
sol()안의 네 개의 재귀함수의 동작이 DFS 개념임.
'''
n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))
maxi, mini = -1000000000, 1000000000

def sol(index,total,add,sub,mul,div):
    global maxi, mini
    if index == n-1:
        maxi = max(maxi, total)
        mini = min(mini, total)
        return
    if add>0:
        sol(index+1, total+num[index+1], add-1, sub, mul, div)
    if sub>0:
        sol(index+1, total-num[index + 1], add, sub-1, mul, div)
    if mul>0:
        sol(index+1, total*num[index + 1], add, sub, mul-1, div)
    if div>0:
        sol(index+1, int(total/num[index + 1]), add, sub, mul, div-1)

sol(0,num[0],op[0],op[1],op[2],op[3])
print(maxi,mini,sep='\n')
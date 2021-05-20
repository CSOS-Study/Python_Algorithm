n = int(input())
ine_sing = list(map(str,input().split()))

visited = [False]*10
max_ans =""
min_ans =""

def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j

def solve(idx,s):
    global max_ans,min_ans

    if(idx==n+1):
        if(len(min_ans)==0):
            min_ans = s
        else:
            max_ans = s
        return
    for i in range(10):
        if not visited[i]:
            if(idx==0 or check(s[-1],str(i),ine_sing[idx-1])):
                visited[i]=True
                solve(idx+1,s+str(i))
                visited[i]=False


solve(0,"")
print(max_ans)
print(min_ans)
import sys
lst=[]
for i in range(10):
    n=int(sys.stdin.readline())
    lst.append(n%42)
print(len(set(lst)))

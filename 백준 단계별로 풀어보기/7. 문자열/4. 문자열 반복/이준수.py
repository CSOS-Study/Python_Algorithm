n = int(input())
for _ in range(n):
    r , s= input().split()
    for c in s:
        print(int(r)*c,end='')
    print()
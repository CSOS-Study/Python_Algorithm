import sys
n = int(input())

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    ## 자주입출력 해야할때는 이런거 써야한다..
    ## 이걸로 통일하는게 좋다
    print(a+b)
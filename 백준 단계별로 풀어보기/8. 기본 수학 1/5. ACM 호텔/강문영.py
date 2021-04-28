n = int(input())
for i in range(n):
    height, width, host = map(int, input().split())
    if host % height != 0:
        print(str(host % height*100 + (host // height + 1)))
    else:
        print(str(height*100 +(host//height)))

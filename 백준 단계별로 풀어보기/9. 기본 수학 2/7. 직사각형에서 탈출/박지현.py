x,y,w,h = map(int, input().split())
lst = [w-x, h-y,x,y]
print(min(lst))
'''
어느 한점에서 변까지의 상하좌우 거리중 가장 작은 거리를 반환.
'''

x, y, w, h = map(int, input().split())
print(min(x,y,w-x,h-y))
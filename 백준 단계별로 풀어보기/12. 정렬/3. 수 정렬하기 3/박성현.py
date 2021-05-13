import sys

arr = [0]*100001
for _ in range(int(sys.stdin.readline())):
    arr[int(sys.stdin.readline())] += 1
for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)
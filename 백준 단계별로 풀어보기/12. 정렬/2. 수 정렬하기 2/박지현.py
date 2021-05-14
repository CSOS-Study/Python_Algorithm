'''
시간복잡도 O(nlog n) 으로 푸는 것을 권장
sort()는 O(nlog n)

input()으로하면 시간초과 -> sys.stdin.readline()으로 풀기
'''

import sys
lst=[]
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in lst: print(i)
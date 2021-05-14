'''
메모리 문제
1) sys로 입력 받기
2) 10001개 크기의 배열 미리 생성하기
'''
import sys
count_lst=[0] * 10001

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    count_lst[num] +=1

for i in range(len(count_lst)):
    if count_lst[i] != 0:
        for j in range(count_lst[i]):
            print(i)
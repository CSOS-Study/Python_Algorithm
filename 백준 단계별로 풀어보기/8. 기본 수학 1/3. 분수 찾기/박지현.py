'''
n번째 대각선에 n개의 분수가 있음
짝수번째 대각선일 때 : 분자 오름차순/분모 내림차순
홀수번째 대각선일 때 : 분자 내림차순/분모 오름차순

1번째 대각선 : 1개
2번째 대각선 : 2개 //2~3번 분수를 가짐
3번째 대각선 : 3개 //4~6번 분수를 가짐
4번째 대각선 : 4개 //7~10번 분수를 가짐
'''

X,num,i = int(input()), 2, 1
if X==1 :
    print(f'{1}/{1}')
    exit()
else:
    while True:
        if X <= num+i: break # X가 속한 i+1번째 대각선
        else:
            i+=1
            num+=i
inx = X-num # X가 대각선에 위치한 인덱스 : inx
A = inx + 1
B = (i + 1) - inx

if (i+1) % 2 ==0: print(f'{A}/{B}')
else: print(f'{B}/{A}')
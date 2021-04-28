'''
1     ...
1  6  21  56
1  5  15  35
1  4  10  20
1  3  6   10
1  2  3   4   5   6   7
'''

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    f_0 = [i for i in range(1,n+1)]
    # 0층 사람 수(n호 까지만 알면됨)
    # n개의 원소가 들어감 (1호 ~ n호)
    for _ in range(k): #층만큼 돈다
       for b in range(1,n): # n호까지 구해야함 == index는 n-1까지
           f_0[b] += f_0[b-1]
    print(f_0[n-1])
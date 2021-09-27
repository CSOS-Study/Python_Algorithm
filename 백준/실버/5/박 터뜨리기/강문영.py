n,k = map(int, input().split())

if k>n:
    print(-1)
else:
    sum_ = sum(range(1,k+1))
    n = n-sum_
    if n%k ==0:
        print(k -1)
    elif n<0:
        print(-1)
    else: #n>0
        print(k)





    # 이렇게하면 mod는 반드시 k보다 작다. mod는 k-1개까지만 가능
    # 공의 개수가 모두 다르려면 최소 1차이가 나야한다.

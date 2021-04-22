T = int(input())
for _ in range(T):
    n, S = input().split()
    s_lst = list(S)
    for i in range(0, len(s_lst)):
        print(s_lst[i]*int(n),end='')
    print()
def desum(N:int):
    for M in range(1, N+1):
        if N == M + sum(map(int, str(M))):
            return M
    return 0


print(desum(int(input())))

#for else  : break문을 만나지 않으면 else문으로 떨어진다.
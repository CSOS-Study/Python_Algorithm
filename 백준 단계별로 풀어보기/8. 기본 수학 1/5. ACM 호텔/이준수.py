T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N % H if N % H else H
    X = (N + H - 1) // H
    print("{}{:02d}".format(Y,X))
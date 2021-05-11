N = int(input())
figure = [tuple(map(int, input().split())) for _ in range(N)]

for i, fig_1 in enumerate(figure):
    k = 1
    for j, fig_2 in enumerate(figure):
        if i != j and fig_1[0] < fig_2[0] and fig_1[1] < fig_2[1]:
            k += 1
    print(k, end=' ')
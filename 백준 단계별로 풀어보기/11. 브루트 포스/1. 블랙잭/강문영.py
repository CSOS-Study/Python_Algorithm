n, m = map(int, input().split())
n_list = list(sorted(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            temp = n_list[i] + n_list[j] + n_list[k]
            if result < temp <= m:
                result = temp

print(result)
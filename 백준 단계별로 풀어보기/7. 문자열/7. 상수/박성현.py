n = list(map(str, input().split()))
a, b = str(n[0][::-1]), str(n[1][::-1])
print(a if a > b else b)

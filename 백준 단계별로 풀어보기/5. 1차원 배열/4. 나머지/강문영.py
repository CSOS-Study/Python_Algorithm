distinct_list = set()

for _ in range(0,10):
    n = int(input())
    distinct_list.add(n%42)

print(len(distinct_list))
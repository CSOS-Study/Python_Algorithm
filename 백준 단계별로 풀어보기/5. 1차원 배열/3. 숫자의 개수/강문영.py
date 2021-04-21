n = int(input())*int(input())*int(input())
result_list = [0 for _ in range(0,10)]

for i in str(n):
    result_list[int(i)] += 1

for i in result_list:
    print(i)


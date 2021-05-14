n = int(input())
ordered_dict = []
for i in range(n):
    x, y = map(int,input().split())
    ordered_dict.append([x,y])

ordered_dict.sort()

for x,y in ordered_dict:
    print(x,y)

    # "aaa" , "abc" ,"abb"
import collections
target_alpha = input().upper()
answer = collections.Counter(list(target_alpha)).most_common()
if len(answer) == 1:
    print(target_alpha)
else:
    if answer[0][1] == answer[1][1]:
        print("?")
    else:
        print(answer[0][0])

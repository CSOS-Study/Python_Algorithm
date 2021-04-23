def is_group_word(word):
    stack = []
    for i,c in enumerate(word):
        if c not in stack:
            stack.append(c)
        else:
            if(i!=0) & (word[i] != word[i-1]):
                return 0
    return 1

n = int(input())
result = 0
for _ in range(n):
    result += is_group_word(input())

print(result)
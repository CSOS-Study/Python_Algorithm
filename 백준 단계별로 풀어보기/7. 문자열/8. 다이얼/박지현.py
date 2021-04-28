W = input().lower()
word_lst = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in range(len(W)):
    for word in word_lst:
        if W[i] in word:
            time += word_lst.index(word) + 3
print(time)
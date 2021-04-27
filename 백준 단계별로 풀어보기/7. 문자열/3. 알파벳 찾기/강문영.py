from string import ascii_lowercase
target_string = input()
alpha_list = list(ascii_lowercase)

for i in alpha_list:
    if i in target_string:
        print(target_string.index(i))
    else:
        print(-1)
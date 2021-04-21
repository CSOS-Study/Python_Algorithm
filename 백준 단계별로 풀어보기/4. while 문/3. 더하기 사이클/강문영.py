# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다.
# 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
n = int(input())
result = n
cnt = 0

# while True:
#     if result<10:
#         a = 0
#         b = result
#     else:
#         a,b = map(int,str(result))
#
#     result = int(str(b) + str(a + b)[-1])
#     cnt +=1
#
#     if result == n:
#         break

while True:
    temp = n//10 + n%10
    new_result = (n%10)*10 + temp%10

    cnt += 1
    n = new_result

    if new_result == result:
        break

print(cnt)
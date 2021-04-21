n = int(input())

def confirm_score(result):
    result_score = 0
    cnt = 0
    for i in result:
        if i == 'O':
            cnt += 1
        else:
            result_score += sum(range(1, cnt + 1))
            cnt = 0

    result_score += sum(range(1, cnt + 1))

    return result_score

for _ in range(n):
    result = input()
    print(confirm_score(result))

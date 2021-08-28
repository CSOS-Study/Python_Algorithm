def solution(s):
    stack = []
    for c in s:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    if stack:
        return 0
    else:
        return 1

## for 루프를 돌면서 제거하는 건데, 앞쪽에 baa가 있다면, aa가 제거되고 나서 인덱스 이동이 앞쪽인데 b는 어떻게 제거함?
# 아.. 같으면 두개를 집어넣는게 아니라 앞쪽에 있는 것을 제거하기 때문에, b가 -1 즉, 맨 뒤로 오게되고 다시 b 기준으로 비교를 하게됨
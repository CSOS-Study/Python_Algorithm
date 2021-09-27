def solution(n):
    # 먼저 1부터 더해서 15가 되는 범위를 파악하기
    # 투포인터로 간다!!!!!!!!
    a = [i for i in range(1, n + 1)]
    target = n
    left, right = 0, 0
    cnt = 0
    tot = 0

    while left < len(a):
        if tot == target:
            cnt += 1
            tot -= a[left]
            left += 1
        elif tot > target or right >= len(a):  # 이 부분율 유심히 보길 바란다.
            tot -= a[left]
            left += 1
        elif tot < target:
            tot += a[right]
            right += 1

    return cnt
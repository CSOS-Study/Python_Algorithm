def dfs(marbles:list):
    if len(marbles) == 2:
        return 0
    return max(marbles[idx - 1] * marbles[idx + 1] + dfs(marbles[:idx] + marbles[idx + 1:])
               for idx in range(1, len(marbles)-1))

N = int(input())
marbles = list(map(int, input().split()))
print(dfs(marbles))
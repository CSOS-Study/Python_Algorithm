def dfs(n, nums):
    if (n < 4):
        return str(nums[n % 3 - 1])
    if (n % 3 == 0):
        n = n - 3
    return dfs(n // 3, nums) + dfs(n % 3, nums)

def solution(n):
    nums = [1, 2, 4]
    return dfs(n, nums)


# def solution(n):
#     nums = [1, 2, 4]
#     answer = ''
#     while (n > 0):
#         n -= 1
#         answer = str(nums[n % 3]) + answer
#         n = n // 3
#     return answer

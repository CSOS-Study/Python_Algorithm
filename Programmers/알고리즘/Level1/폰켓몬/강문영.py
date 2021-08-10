def solution(nums):
    max_pocket_kinds = len(set(nums))
    pick_nums = len(nums) // 2

    if max_pocket_kinds >= pick_nums:
        return pick_nums

    return max_pocket_kinds


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_num = max(nums, default=0)

        for candidate in range(1, max_num + 1):
            if candidate not in num_set:
                return candidate
        return max(1, max_num + 1)
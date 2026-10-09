class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n):
            left = (i - k < 0) or (nums[i] > nums[i - k])
            right = (i + k >= n) or (nums[i] > nums[i + k])
            
            if left and right:
                ans += nums[i]
                
        return ans
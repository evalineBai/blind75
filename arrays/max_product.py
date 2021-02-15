class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        current_max = nums[0]
        current_min = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], current_max * nums[i], current_min * nums[i])
            current_min = min(nums[i], current_max * nums[i], current_min * nums[i])
            current_max = temp
            max_prod = max(current_max, max_prod)
        return max_prod
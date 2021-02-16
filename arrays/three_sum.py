class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i, val in enumerate(nums):
            if val <= 0:
                if (i == 0) or (val != nums[i - 1]):
                    self.twoSum(i, nums, output)
        return output
    
    def twoSum(self, i: int, nums: List[int], output: List[int]) -> List[int]:
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
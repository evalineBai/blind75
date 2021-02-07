class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            if val in dic.keys():
                return [dic[val], i]
            else:
               dic[target - val] = i
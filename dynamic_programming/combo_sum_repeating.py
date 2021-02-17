class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0 for i in range(target + 1)]
        cache[0] = 1
        for curr_sum in range(target + 1):
            for num in nums:
                if curr_sum - num >= 0:
                    cache[curr_sum] += cache[curr_sum - num]
        return cache[target]
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for val in nums:
            if val in numset:
                return True
            numset.add(val)
        return False
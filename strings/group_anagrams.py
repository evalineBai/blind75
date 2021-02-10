class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for val in strs:
            sorted_str = ''.join(sorted(val))
            if sorted_str in dicts:
                dicts[sorted_str].append(val)
            else:
                dicts[sorted_str] = [val]
        return dicts.values()

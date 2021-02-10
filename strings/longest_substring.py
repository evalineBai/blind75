class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        char_dict = {}
        for i, char in enumerate(s):
            if char in char_dict:
                char_dict[char] += 1
                if char_dict[char] > start:
                    start = char_dict[char]
            longest = max(longest, i - start + 1)
            char_dict[char] = i
        return longest
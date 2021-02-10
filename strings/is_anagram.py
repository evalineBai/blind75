class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chardict = {}
        for char in s:
            if char in chardict:
                chardict[char] += 1
            else:
                chardict[char] = 1
        for char in t:
            if char in chardict:
                chardict[char] -= 1
                if chardict[char] < 0:
                    return False
            else:
                return False
        return True if sum(chardict.values()) == 0 else False
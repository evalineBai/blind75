class Solution:
    def isValid(self, s: str) -> bool:
        matches = { ")": "(", "}": "{", "]": "[" }
        stack = []
        for char in s:
            if char in matches:
                current = stack.pop() if stack else '#'
                if matches[char] != current:
                    return False
            else:
                stack.append(char)
        return not stack

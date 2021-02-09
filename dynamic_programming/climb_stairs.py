class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        combos = [0, 1, 2]
        for i in range(3, n + 1):
            combos.append(combos[i - 1] + combos[i - 2])
        return combos[n]
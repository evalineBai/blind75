import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [math.inf] * (amount + 1)
        cache[0] = 0
        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    cache[val] = min(cache[val], 1 + cache[val - coin])
        return cache[amount] if cache[amount] != math.inf else -1
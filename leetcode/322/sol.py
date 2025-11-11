from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            if dp[i] != -1:
                continue
        
                
            choose_min_from = []

            for coin in coins:
                if i - coin > 0 and dp[i - coin] != -1:
                    choose_min_from.append(dp[i - coin] + 1)

            if choose_min_from:
                dp[i] = min(choose_min_from)
        
        return dp[amount]
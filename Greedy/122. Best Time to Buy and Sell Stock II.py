class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            a = prices[i] - prices[i-1]
            if a>0:
                res += a
        return res

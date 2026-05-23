class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i, p in enumerate(prices[1:]):
            res = max(res, p - buy)
            buy = min(buy, p)
        return res

            
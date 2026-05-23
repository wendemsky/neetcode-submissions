class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l: buy, r: sell
        maxP = 0
        
        while r < len(prices):
            # profit
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP


            
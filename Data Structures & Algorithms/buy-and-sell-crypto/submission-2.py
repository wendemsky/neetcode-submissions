class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l: buy, r: sell
        maxP = 0
        
        while r < len(prices):
            # profit: calc maxP and increment r
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            # loss: set l to new low -> r and increment r
            else:
                l = r
            r += 1
        return maxP


            
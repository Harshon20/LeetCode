class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sell=0
        profit=0

        for i in range(1,len(prices)):
            sell=prices[i]-buy
            profit=max(profit,sell)
            buy=min(prices[i],buy)
        return profit    
        
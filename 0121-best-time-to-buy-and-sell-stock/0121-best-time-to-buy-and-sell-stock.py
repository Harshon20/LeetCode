class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        sell=0

        for price in prices:
            if price<buy:
                buy=price
            elif sell<price-buy:
                sell=price-buy
        return sell               
        
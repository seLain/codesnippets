class Solution:
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        else:
            price_in = prices[0]
            price_out = price_in
            for price in prices[1:]:
                if price > price_in:
                    diff = price - price_in
                    if diff > max_profit:
                        max_profit = diff
                        price_out = price
                elif price < price_in:
                    price_in = price
            return max_profit
                

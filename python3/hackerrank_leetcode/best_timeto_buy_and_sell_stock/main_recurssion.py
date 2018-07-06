class Solution:
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest_price, max_profit = self.recur_max_profit(prices)
        return max_profit

    def recur_max_profit(self, prices):

        if len(prices) == 0:
            return 0, 0
        elif len(prices) == 1:
            return prices[0], 0
        else:
            price_in = prices[0]
            highest_price, max_profit = self.recur_max_profit(prices[1:])
            temp_profit = highest_price - price_in
            if temp_profit > max_profit:
                max_profit = temp_profit
            if price_in > highest_price:
                highest_price = price_in
            return highest_price, max_profit

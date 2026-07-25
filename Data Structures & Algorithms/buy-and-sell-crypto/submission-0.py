class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest =prices[0]
        highest_profit =0
        for price in prices:
            if price <lowest:
                lowest=price
            
            profit = price-lowest
            if profit> highest_profit:
                highest_profit = profit
        return highest_profit
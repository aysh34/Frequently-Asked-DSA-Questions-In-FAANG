class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")  
        max_profit = 0  
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i] 
            else:
                profit = prices[i] - min_price  # Calculate profit
                max_profit = max(max_profit, profit) 
        
        return max_profit
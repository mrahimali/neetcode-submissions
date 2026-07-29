class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        day = 0
        while day <= len(prices)-1:
            for i in range(day+1, len(prices)):
                prof = prices[i]-prices[day]
                if prof>profit:
                    profit = prof
            day+=1
        
        return profit
                
        
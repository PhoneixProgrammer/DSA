class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        profit = 0

        for i in range(len(prices)):
            if prices[i] < min_val :
                min_val = prices[i]
            elif prices[i] - min_val > profit :
                profit = prices[i]-min_val

        return profit 
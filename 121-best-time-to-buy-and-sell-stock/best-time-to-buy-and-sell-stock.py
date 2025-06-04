class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Brute force Approach :  passed 199/212 test cases
        # time limit exceeded
        max_value = 0 
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i] :
                    max_value = max(max_value,prices[j]-prices[i])
        return max_value
        '''

        min_price =  float('inf') #Tracks the lowest price seen so far
        max_profit = 0 # track the maximum profit found

        for price in prices : 
            if price < min_price :
                min_price = price # updates the min_price if the current_price is lower
            else : 
                #calculate profit if sold today and update max_profit if better
                max_profit = max(max_profit, price - min_price)
        return max_profit
            

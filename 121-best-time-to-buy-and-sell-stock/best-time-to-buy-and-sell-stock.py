class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        profit = 0

        for price in prices :
            if price < min_val :
                min_val = price 
            else :
                profit = max(profit, price-min_val)

        return profit 

        '''
        | Complexity Type  | Value    | Explanation                        |
| ---------------- | -------- | ---------------------------------- |
| Time Complexity  | **O(n)** | Single pass through prices         |
| Space Complexity | **O(1)** | Only constant extra variables used |

'''
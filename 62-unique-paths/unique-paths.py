class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[j] represents number of paths to reach column j in current row 
        dp = [1] * n # first row is all 1s

        for i in range(1,m) :
            for j in range(1,n) :
                dp[j] += dp[j-1]
        return dp[-1]

        # T.C : O(m*n)
        # S.C : O*1
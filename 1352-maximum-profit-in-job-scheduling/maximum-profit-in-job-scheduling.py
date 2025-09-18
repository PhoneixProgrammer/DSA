class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Dynamic Programming with Binary search
        
        #step 1 : sort jobs by end time 
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x : x[1])
        ends = [job[1] for job in jobs] #to use binary search 

        #step 2: DP array 
        n = len(jobs)
        dp = [0]*n

        for i in range(n):
            curr_profit = jobs[i][2]
            #binary search for last job ending <= start of current
            index = bisect_right(ends, jobs[i][0]) - 1
            if index != -1 :
                curr_profit += dp[index]
            #max of taking or skipping current job
            dp[i] = max (curr_profit,dp[i-1] if i > 0 else 0)
        return dp[-1]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack (start,current,total):
            if total == target :
                result.append(current[:])
                return

            if total > target : 
                return 

            for i in range(start,len(candidates)) :
                num = candidates[i]
                current.append(num)
                #not i+1 -- > because we can reuse same number 
                backtrack(i,current,total+num)
                current.pop() #backtrack  

        backtrack(0,[],0)
        return result
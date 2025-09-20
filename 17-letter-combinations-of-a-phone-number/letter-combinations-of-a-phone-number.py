class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res= []
   

        numbers_map = {"1" : "", "2": "abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        #Backtracking Algorithm 
        def backtrack(i, curStr) :
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            for c in numbers_map[digits[i]]:
                backtrack(i+1, curStr + c) #1,a

        if digits : 
            backtrack(0,"")

        return res        

        '''
        Summary Table
Aspect	Complexity
Time	O(n * 3^m * 4^k) → worst-case O(n * 4^n)
Space	O(n * 3^m * 4^k) → dominated by output
Recursion depth	O(n)
'''
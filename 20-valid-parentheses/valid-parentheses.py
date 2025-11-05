class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {'(': ')', '{': '}', '[':']'}

        for char in s :
            if char in brackets_dict : 
                stack.append(char)
                
            elif stack and char == brackets_dict[stack[-1]]:
                stack.pop()
            else:
                return False
           
        
        if len(stack) == 0  :
            return True
        else :
            return False

        #T.C  and S.C : O(n)
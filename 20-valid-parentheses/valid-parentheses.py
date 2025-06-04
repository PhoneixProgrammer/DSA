class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','{':'}','[':']'}
        stack = []

        for char in s :
            if char in pairs :  
                #If it's an opening bracket
                stack.append(char)
            else : # its a closing braket
                if not stack : #case when no opening bracket available
                    return False
                top = stack.pop() #pop the last elemnt
                if pairs[top] != char : #check if it matches the closing bracket
                    return False
        return len(stack) == 0      

        # t.c  :  O(n)
        # s.c : O(n)

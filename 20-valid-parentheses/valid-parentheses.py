class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','{':'}','[':']'}
        stack = []

        for ch in s :
            if ch in pairs : 
                stack.append(ch)
            else : 
                #case when there is no opening bracket , found closing bracket 
                if not stack :
                    return False
                
                top_ch =  stack.pop()
                if pairs[top_ch]!=ch :
                    return False
        return len(stack)==0
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_hashmap = {'(':')','{':'}','[':']'}

        stack = []

        for char in s :
            if char in brackets_hashmap :
                stack.append(char)
            else : 
                if not stack :
                    return False
                last_open = stack.pop()
                if brackets_hashmap[last_open] != char : 
                    return False

        return len(stack)==0

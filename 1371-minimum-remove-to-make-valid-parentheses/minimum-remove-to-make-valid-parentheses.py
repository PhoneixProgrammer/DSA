class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #First Pass : remove invalid ')'
        res = []
        open_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1
                res.append(ch)
            elif ch == ')':
                if open_count > 0:
                    open_count -= 1
                    res.append(ch)
                # else skip this ")"
            else :
                res.append(ch)

        #Second Pass : remove extra '(' from right to left
        final = [] 
        open_count = 0
        for ch in reversed(res):
            if ch == ")":
                open_count += 1
                final.append(ch)
            elif ch == "(":
                if open_count > 0 :
                    open_count -= 1
                    final.append(ch)
            else:
                final.append(ch)
        return ''.join(reversed(final))
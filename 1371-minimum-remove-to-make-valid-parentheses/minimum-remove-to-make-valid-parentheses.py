class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # First Pass:  remove excess ")" from left to right
        res = []
        open_count = 0
        for c in s :
            if c == "(":
                open_count += 1
                res.append(c)
            elif c == ")":
                if open_count > 0:
                    open_count -= 1
                    res.append(c)
            else:
                res.append(c)

        # Second Pass : remove excess "(" from right to left
        final = []
        open_count = 0
        for c in reversed(res):
            if c == ")":
                open_count += 1
                final.append(c)
            elif c == "(":
                if open_count > 0 :
                    open_count -= 1
                    final.append(c)
            else:
                final.append(c)
        
        return ''.join(reversed(final))
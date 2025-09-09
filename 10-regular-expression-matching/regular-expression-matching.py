class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        # check if first character matches
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
        
        if len(p) >= 2 and p[1] == '*':
            # Case 1: skip the "x*" part → self.isMatch(s, p[2:])
            # Case 2: consume one char if first matches → self.isMatch(s[1:], p)
            return (self.isMatch(s, p[2:]) or
                    (first_match and self.isMatch(s[1:], p)))
        else:
            # move forward if first chars match
            return first_match and self.isMatch(s[1:], p[1:])

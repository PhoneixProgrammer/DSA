class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left_p = 0
        right_p = len(s)-1

        while left_p < right_p :
            if s[left_p] == s[right_p]:
                left_p+=1
                right_p -= 1
            else :
                return False
        return True
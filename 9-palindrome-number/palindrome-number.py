class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0
        if x < 0  or (x%10 == 0 and x!=0):
            return False

        reversed_half = 0
        while x > reversed_half : 
            digit = x%10 
            reversed_half = reversed_half*10 + digit
            x = x // 10
        return x == reversed_half or x == reversed_half//10
        '''

        x= str(x)
        left = 0
        right = len(x)-1

        while left < right : 
            if x[left] != x[right]:
                return False
            left +=1 
            right -=1
        return True

        # Time Complexity : O(n)
        #Space Complexity : O(n)
        '''
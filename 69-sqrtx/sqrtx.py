class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 :
            return x # as sqrt (0) =0 and sqrt(1)=1
        
        left = 1
        right =  x//2 # no need to check beyond this point as sqrt is usually  half of the number

        while left<=right :
            mid = (left+right)//2
            if mid*mid == x : #condition for perfect square
                return mid
            elif mid*mid < x:
                left = mid + 1 #go right to find a bigger candidate
            else:
                right = mid -1 #go left to find a smaller candidate
        #when the loop ends, right is the integer part of sqrt(x)
        return right

        # t.c : O(logx) as it is binary search
        # s.c : O(1)
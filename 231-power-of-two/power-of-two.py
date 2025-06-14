class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n > 0 :
            x = math.log2(n)
        else : 
            return False
        if x.is_integer():
            return True
        else:
            return False 
           
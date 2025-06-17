import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n > 0 :
            res = math.log(n)/math.log(3)
            return abs(res - round(res)) < 1e-10  # Tolerance check
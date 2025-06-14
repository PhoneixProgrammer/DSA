class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0 :
            if n & 1:
                count+=1
            n >>= 1
        return count

        #t.c: O(b) ; b is the number of bits if it si 32 or 64 bits
        #s.c : O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        #step1 : convert the n into 32 bit binary format string
        binary = bin(n)[2:].zfill(32)

        #step 2 :  reverse the binary string 
        reversed_binary = binary[::-1]

        #step 3: convert back to integer
        return int(reversed_binary,2)


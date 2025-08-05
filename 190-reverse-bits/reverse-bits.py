class Solution:
    def reverseBits(self, n: int) -> int:
        binary_number = bin(n)[2:].zfill(32)
        #print(binary_number)

        reversed_binary_number = binary_number[::-1]

        return int(reversed_binary_number,2)
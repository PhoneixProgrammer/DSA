class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        
        hex_chars = "0123456789abcdef"
        result = ""

        if num < 0 :
            num += 2 ** 32

        while num > 0:
            reminder = num % 16 
            result = hex_chars[reminder] +result
            num //= 16
        return result
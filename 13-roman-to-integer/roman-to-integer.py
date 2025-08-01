class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I":1,"V":5,"X" :10,"L": 50, "C": 100,"D" :500,"M":1000}
        total = 0
        prev = 0
        for i in range(len(s)-1,-1,-1 ) :
            ch = s[i]
            val = roman_dict[ch]
            if val < prev :
                total -= val
            else:
                total+=val
            prev = val
        return total
        '''
        roman_dict = {"I":1,"V":5,"X" :10,"L": 50, "C": 100,"D" :500,"M":1000}
        total = 0 
        prev = 0
        for ch in reversed(s):
            val = roman_dict[ch]
            if val < prev :
                total -= val
            else:
                total+=val
            prev = val
        return total
        #Time Complexity : o(n)
        #Space Complexity : O(1)
        '''

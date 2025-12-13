class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''

        #Sliding Window Technique
        charSet = set() # to store each character 
        left = 0 # left pointer is to delete from left when a repeating charcter is found
        res = 0 # to store the length of the substring

        for right in range(len(s)):
            while s[right] in charSet: #if the chracter is in the charSet
                charSet.remove(s[left]) # removing the chracter from left in th chrSet window
                left += 1
            charSet.add(s[right])
            res = max(res, right-left+1)
        return res'''

        charSet = set()

        left = 0
        
        res =0 

        for char in range(len(s)):
            while s[char] in charSet :
                charSet.remove(s[left])
                left += 1
            charSet.add(s[char])
            res = max(res,char-left+1)
        return res
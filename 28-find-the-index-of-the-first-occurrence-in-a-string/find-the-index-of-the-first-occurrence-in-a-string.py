class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if n == 0 :
            return -1
        
        for i in range(m-n+1):#only check till m-n
            j=0
            while j<n and haystack[i+j]==needle[j]:
                j+=1
            if j == n:
                return i
        return -1
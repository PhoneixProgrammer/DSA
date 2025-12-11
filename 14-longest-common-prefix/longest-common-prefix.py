class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs :
            return ""
        
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix :
                    return ""
        return prefix

        # Time Complexity : O(n*k)
        # -- >  n = length of strs and k is the number of characters in prefix

        #Space Complexity : O(k)
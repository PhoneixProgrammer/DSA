class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #edge case if the length of strs is 0
        if len(strs) == 0:
            return ""
        
        #horizontal scanning 
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix :
                    return ""
        return prefix

        #time complexity 
        # O(n*m^2)
        #s.c : O(1)
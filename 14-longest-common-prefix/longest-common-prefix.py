class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : 
            return ""

        for i in range(len(strs[0])):
            char =  strs[0][i] # character to compare
            for s in strs[1:]:
                if i >= len(s) or s[i]!=char:
                    return strs[0][:i] #return prefix found so far
        return strs[0] #all characters matched

        #Time Complexity : O(MxN)
        # Space Complexity : O(1)
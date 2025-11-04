class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1,len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
        return prefix

        #tIme Complexity : O(n*m)
        # -- n is lengths of the strs
        # --- m is the length of the first string or prefix 
        #Space Complexity : O(1)
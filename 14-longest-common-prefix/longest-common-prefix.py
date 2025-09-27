class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(common_prefix) :
                common_prefix = common_prefix[:-1]
        return common_prefix

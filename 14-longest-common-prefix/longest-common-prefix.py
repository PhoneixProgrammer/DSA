class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""

        
        result = strs[0]
        for i in strs[1:]:
            while not i.startswith(result) :
                result =  result[:-1]
                if not result :
                    return ""
        return result
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs : #O(n)
            key = "".join(sorted(s)) # dominated : O(klogk) becasue python ibuilt uses timsort
            group_anagrams[key].append(s)

        return list(group_anagrams.values())

        #overall time complexity : O(n*k log k)
        #space complexity : O(n*k) --> k is from the line 6, where new string is created 
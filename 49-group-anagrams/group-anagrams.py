class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs : #O(n)
            key = "".join(sorted(s)) # dominated : O(klogk) becasue python ibuilt uses timsort
            group_anagrams[key].append(s)

        return list(group_anagrams.values())

        #overall time complexity : O(n*k log k)
        #space complexity : O(n*k) --> k is from the line 6, where new string is created 



        ''' TO DO : to understand the ord well
        from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs:  # O(n)
            # Build frequency count: O(k)
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            # Tuple is immutable → hashable key
            # Space: O(26) = O(1)
            group_anagrams[tuple(count)].append(s)

        # O(n) to collect results
        return list(group_anagrams.values())
'''
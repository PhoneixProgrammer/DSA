class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = []

        for start,end in intervals :
            #no overlap , then merge
            if not merged or merged[-1][1] < start :
                merged.append([start,end])
            else :
                merged[-1][1] = max(merged[-1][1],end)
        return merged 
        '''
        | Step                   | Time Complexity | Space Complexity |
| ---------------------- | --------------- | ---------------- |
| Sort intervals         | O(n log n)      | O(log n)         |
| Merge loop             | O(n)            | O(1)             |
| Store merged intervals | —               | O(n)             |
| **Total**              | O(n log n)      | O(n)             |

'''
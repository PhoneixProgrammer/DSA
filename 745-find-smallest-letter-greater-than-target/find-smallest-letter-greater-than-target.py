class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        lo, hi = 0,n
        while lo < hi :
            mid =(lo+hi)//2
            if letters[mid] <= target :
                lo = mid +1
            else : 
                hi = mid
        return letters[0] if lo == n else letters[lo]
        '''
        Step-by-step idea

Let n = len(letters).

Binary search on indices [0, n) maintaining the invariant:

lo is the first index we haven’t ruled out,

hi is the first index that could still be the answer.

At each step:

Compute mid = (lo + hi) // 2.

If letters[mid] <= target, the answer must be to the right of mid → set lo = mid + 1.

Else letters[mid] > target, mid could be the answer → set hi = mid.

When the loop ends, lo == hi is the index of the first letter > target.

If lo == n (no such letter), wrap around and return letters[0].
'''
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
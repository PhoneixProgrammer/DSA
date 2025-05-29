class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count ={}
        for num in nums :
            if num in count:
                count[num] = count[num] + 1
            else :
                count [num] = 1
        
        for value in count.values():
            if value > 1 :
                return True 
        return False

        # t.c : O(n) and s.c : O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        unique_nums=[]
        seen=set()
        for num in nums :#O(n)  time
            if num not in seen:
                seen.add(num)
                unique_nums.append(num)
        unique_nums = sorted(unique_nums, reverse=True) #O(nlogn)
        if len(unique_nums)>2: #O(1)
            return unique_nums[2]
        else:
            return max(unique_nums)

        #t.c : O(nlogn)
        '''

        #Optimal Solution : O(n)
        first = second = third = None

        for num in nums :
            if num ==  first or num == second or num == third :
                continue
            
            if first is None or num > first :
                third = second
                second = first
                first = num 
            
            elif second is None or num > second :
                third = second
                second = num
            
            elif third is None or num > third :
                third = num
        
        if third is not None :
            return third
        else:
            return first

        #t.c : O(n)
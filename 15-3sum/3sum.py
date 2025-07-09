class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #Step 1: Sort the array
        res = []
        n = len(nums)

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue #skip duplicate va;ue for i

            left = i + 1
            right =  n-1

            while left < right :
                total = nums[i] + nums[left] + nums[right]

                if total == 0: 
                    res.append([ nums[i], nums[left], nums[right] ])

                    #skip duplicate values for left and right
                    while left < right and nums[left] == nums[left+1] :
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1

                    left += 1 
                    right -= 1


                elif total < 0:
                    left +=1
                else :
                    right -=1
        return res

        #Time Complexity : O(n2)
        # Space Complexity : O(1)
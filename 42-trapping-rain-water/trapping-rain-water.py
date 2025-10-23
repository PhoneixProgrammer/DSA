class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n-1
        left_max , right_max =0 ,0
        water = 0  

        while left < right :
            if height[left] < height[right] :
                if height[left] >= left_max:
                    left_max = height[left]
                else :
                    water += left_max - height[left]
                left += 1

            else :
                if height[right] >= right_max :
                    right_max = height[right]
                else :
                    water += right_max - height[right]
                right -= 1

        return water

        '''
        ⏱️ Time Complexity

O(n) — Each index is processed at most once.

\U0001f9ee Space Complexity

O(1) — Only a few variables are used, no extra arrays.
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if the list is empty, no water can be trapped
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        total = 0
        
        leftMax = height[left]
        rightMax = height[right]
        
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                # No need for extra "if leftMax - height[left] > 0" check
                total += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                # No need for extra "if rightMax - height[right] > 0" check
                total += rightMax - height[right]
                right -= 1
                
        return total



                



        
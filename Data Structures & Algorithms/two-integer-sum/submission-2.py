from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Stores: { value: index }
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in the map, we found the pair!
            if complement in seen:
                # seen[complement] comes first because it appeared earlier in the array
                return [seen[complement], i]
            
            # Otherwise, record the current number and its index
            seen[num] = i

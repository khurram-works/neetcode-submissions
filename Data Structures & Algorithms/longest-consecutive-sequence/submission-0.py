class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums) # O(1) lookups
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the absolute START of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Keep counting matching consecutive elements forward
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

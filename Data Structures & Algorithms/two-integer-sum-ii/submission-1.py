# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         # seen = {}

#         # for i, num in  enumerate(numbers):
#         #     complement = target - num
#         #     if complement in seen:
#         #         return [seen[complement], i]
            
#         #     seen[num] = i

#         left = 0
#         right = len(numbers)-1

#         while left <= right:
#             if numbers[left]+numbers[right] == target:
#                 return [numbers[left], numbers[right]]
#             elif numbers[left]+numbers[right]>target:
#                 right-=1
#             else:
#                 left+=1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

            
                



        
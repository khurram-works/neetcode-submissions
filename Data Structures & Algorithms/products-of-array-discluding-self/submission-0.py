class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Step 1: Build the Left Products directly into the answer array
        output = [1] * n
        
        # Walk from left to right (Index 1 to n-1)
        # output[i] will hold product of all elements to the left of i
        left_product = 1
        for i in range(n):
            output[i] = left_product   # Store the current left product
            left_product *= nums[i]    # Update for the next index
        
        # Step 2: Walk from right to left and multiply by Right Products
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product  # Multiply the existing left product with the right product
            right_product *= nums[i]    # Update for the next index to the left
        
        return output
    

         
        
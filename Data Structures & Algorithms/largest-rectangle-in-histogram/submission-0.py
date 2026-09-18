class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights+[0]

        max_area = 0
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                height = heights[j]
                left = stack[-1] if stack else -1
                right=i
                width = right - left - 1
                area = height*width
                max_area = max(max_area, area)
            
            stack.append(i)
        
        return max_area

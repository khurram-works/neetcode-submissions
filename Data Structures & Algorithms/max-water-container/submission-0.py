class Solution:

  def maxArea(self, heights: List[int]) -> int:
    max_area = 0  # Avoid shadowing built-in 'max'
    left = 0
    right = len(heights) - 1
    while left < right:
      height = min(heights[left], heights[right])
      width = right - left  # Fixed: right - left instead of left - right
      area = height * width
      if area > max_area:
        max_area = area
      if heights[left] > heights[right]:
        right -= 1
      else:
        left += 1
    return max_area

        
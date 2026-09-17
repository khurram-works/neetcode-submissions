from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()   # stores indices, decreasing values
        result = []

        for right in range(len(nums)):
            # 1. Remove from back: smaller values can never be max
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # 2. Add current index to back
            dq.append(right)

            # 3. Remove from front if out of window
            if dq[0] < right - k + 1:
                dq.popleft()

            # 4. If window is full, record the max (front of deque)
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result

        
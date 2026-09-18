from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k 
                if hours > h:
                    return False
            return True

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
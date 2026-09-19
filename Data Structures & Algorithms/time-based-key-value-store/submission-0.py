from typing import List
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
        # store[key] = list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]
        left = 0
        right = len(entries) - 1
        best = -1

        while left <= right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                best = mid
                left = mid + 1       # try to find a bigger timestamp
            else:
                right = mid - 1      # too big, go left

        if best == -1:
            return ""

        return entries[best][1]
        

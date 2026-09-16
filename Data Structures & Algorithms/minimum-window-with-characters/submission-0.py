# from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)        # need = {"X":1, "Y":1, "Z":1}
        missing = len(t)         # missing = 3

        left = 0
        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            ch = s[right]

            # ---- GRAB ----
            if need[ch] > 0:     # "I still need this letter"
                missing -= 1     # "One less to find"
            need[ch] -= 1        # "I took one"

            # ---- SHRINK ----
            while missing == 0:  # "I have everything"
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                # ---- DROP ----
                left_ch = s[left]
                need[left_ch] += 1   # "I put one back"
                if need[left_ch] > 0: # "I need this again"
                    missing += 1      # "I lost one"
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start : best_start + best_len]
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)  
        missing = len(t)         

        left = 0
        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            ch = s[right]

            if need[ch] > 0:    
                missing -= 1     
            need[ch] -= 1        

            while missing == 0: 
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left


                left_ch = s[left]
                need[left_ch] += 1  
                if need[left_ch] > 0:
                    missing += 1      
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start : best_start + best_len]
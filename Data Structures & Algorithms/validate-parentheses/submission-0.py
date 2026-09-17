class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        st = []

        for ch in s:
            if ch in matching:           
                if not st:
                    return False
                if st[-1] != matching[ch]:
                    return False
                st.pop()
            else:                        
                st.append(ch)

        return len(st) == 0
        
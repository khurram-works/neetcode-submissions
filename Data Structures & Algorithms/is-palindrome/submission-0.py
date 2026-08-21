class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True

        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned_text)-1
        while left <= right :
            if cleaned_text[left] == cleaned_text[right]:
                left += 1
                right -=1
            else:
                return False
        return True
        
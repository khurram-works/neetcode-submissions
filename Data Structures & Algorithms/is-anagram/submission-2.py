class Solution(object):

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # Fixed array of size 26 for 'a' through 'z'
        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1

        # If all counts are back to 0, they are anagrams
        return all(c == 0 for c in counts)
        
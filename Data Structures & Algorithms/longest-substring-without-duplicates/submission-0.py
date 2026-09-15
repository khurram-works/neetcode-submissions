# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if( s == null || s.len()==0):
#             return 0
        
#         left = 0
#         right = 0
#         ans = 0

#         hashset = set()

#         while(right < len(s)):
#             c = s[right]
#             while(c in hashset):
#                 hashset.remove(s[left])
#                 left+=1
#             hashset.add(c)
#             ans = max(ans, right-left+1)
#             right+=1
        
#         return ans

class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    if s is None or len(s) == 0:
      return 0

    left = 0
    ans = 0
    hashset = set()

    for right in range(len(s)):
      c = s[right]
      while c in hashset:
        hashset.remove(s[left])
        left += 1
      hashset.add(c)
      ans = max(ans, right - left + 1)

    return ans



        
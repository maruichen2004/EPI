class Solution:
   # Time: O(len(haystack) - len(needle))
   # Space: O(1)
   def firstSubstr(self, haystack, needle):
      len1, len2 = len(haystack), len(needle)
      if len2 == 0: return haystack
      if len1 < len2: return None
      for i in range(len1 - len2 + 1):
         j, k = i, 0
         while k < len2:
            if haystack[j] == needle[k]:
               j, k = j + 1, k + 1
            else: break
         if k == len2: return haystack[i:]
      return None

if __name__ == "__main__":
   haystack, needle = "Elements of Programming Interviews", "mming"
   t = Solution()
   print t.firstSubstr(haystack, needle)

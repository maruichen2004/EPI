class Solution:
   # Time: O(nlogn)
   # Space: O(m)
   def countOccurrence(self, s):
      res, i, count = [], 0, 1
      s = sorted(s)
      while i < len(s):
         if s[i-1] == s[i]: count += 1
         else:
            res.append((s[i-1], count))
            count = 1
         i += 1
      return res

if __name__ == "__main__":
   s = "befcsaa"
   t = Solution()
   print t.countOccurrence(s)

class Solution:
   # Time: O(n)
   # Space: O(1)
   def celebrityFinding(self, relations):
      i, j = 0, 1
      while j < len(relations):
         if relations[i][j]:
            i = j
            j += 1
         else: j += 1
      return i

if __name__ == "__main__":
   relations = [[False, True, True], [False, False, False], [False, True, False]]
   t = Solution()
   print t.celebrityFinding(relations)

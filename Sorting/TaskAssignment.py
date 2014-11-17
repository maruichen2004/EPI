class Solution:
   # Time: O(nlogn)
   # Space: O(n)
   def taskAssignment(self, A):
      A.sort()
      i, j, res = 0, len(A) - 1, []
      while i < j:
         res.append((A[i], A[j]))
         i, j = i + 1, j - 1
      return res

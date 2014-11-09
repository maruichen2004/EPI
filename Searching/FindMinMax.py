class Solution:
   # Time: O(3/2n)
   # Space: O(1)
   def findMinMax(self, A):
      if len(A) <= 1: return [A[0], A[0]]
      i, cur, res = 2, [0, 0], [A[0], A[1]]
      while i + 1 < len(A):
         if A[i] < A[i+1]: cur = (A[i], A[i+1])
         else: cur = (A[i+1], A[i])
         res[0] = min(res[0], cur[0])
         res[1] = max(res[1], cur[1])
         i += 2
      if len(A) & 1 == 1:
         res[0] = min(res[0], A[-1])
         res[1] = max(res[1], A[-1])
      return res

if __name__ == "__main__":
   A = [1, 5, 3, 7, 0, 2, 6, 8, 4]
   t = Solution()
   print t.findMinMax(A)

class Solution:
   # Time: O(2^n)
   # Space: O(n)
   def combinations(self, A, k):
      res = []
      self.combinationsHelper(res, [], A, k, 0)
      return res

   def combinationsHelper(self, res, cur, A, k, i):
      if len(cur) == k and cur not in res:
         res.append(cur)
      if i < len(A):
         self.combinationsHelper(res, cur, A, k, i+1)
         self.combinationsHelper(res, cur + [A[i]], A, k, i+1)

if __name__ == "__main__":
   A = [1, 2, 3, 4]
   k = 2
   t = Solution()
   print t.combinations(A, k)

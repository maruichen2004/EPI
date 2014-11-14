class Solution:
   # Time: O(2^n)
   # Space: O(n)
   def powerSets(self, A):
      res = []
      self.powerSetsHelper(res, [], sorted(A), 0)
      return res

   def powerSetsHelper(self, res, cur, A, i):
      if i == len(A): res.append(cur)
      if i < len(A):
         self.powerSetsHelper(res, cur, A, i+1)
         self.powerSetsHelper(res, cur + [A[i]], A, i+1)

   def powerSetsDuplicates(self, A):
      res = []
      self.powerSetsDuplicatesHelper(res, [], sorted(A), 0)
      return res

   def powerSetsDuplicatesHelper(self, res, cur, A, i):
      if i == len(A) and cur not in res: res.append(cur)
      if i < len(A):
         self.powerSetsDuplicatesHelper(res, cur, A, i+1)
         self.powerSetsDuplicatesHelper(res, cur + [A[i]], A, i+1)

if __name__ == "__main__":
   A = [1, 2, 3, 4]
   t = Solution()
   print t.powerSets(A)

   B = [1, 1, 2, 3]
   print t.powerSetsDuplicates(B)

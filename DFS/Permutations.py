class Solution:
   # Time: O(n!)
   # Space: O(n)
   def permute(self, A):
      res = []
      self.permuteHelper(res, [], A)
      return res

   def permuteHelper(self, res, cur, A):
      if len(cur) == len(A): res.append(cur)
      for j in range(len(A)):
         if A[j] not in cur:
            self.permuteHelper(res, cur + [A[j]], A)

   def permuteDuplicates(self, A):
      res = []
      visited = [False] * len(A)
      self.permuteDuplicatesHelper(res, [], sorted(A), visited)
      return res

   def permuteDuplicatesHelper(self, res, cur, A, visited):
      if len(cur) == len(A) and cur not in res:
         res.append(cur)
      for j in range(len(A)):
         if visited[j] == False:
            visited[j] = True
            self.permuteDuplicatesHelper(res, cur + [A[j]], A, visited)
            visited[j] = False

if __name__ == "__main__":
   A = [1, 2, 3, 4]
   t = Solution()
   print t.permute(A)

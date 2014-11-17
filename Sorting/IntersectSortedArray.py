class Solution:
   # Time: O(n + m)
   # Space: O(intersect(A, B))
   def intersectSortedArray(self, A, B):
      res, i, j = [], 0, 0
      while i < len(A) and j < len(B):
         if A[i] == B[j] and (i == 0 or A[i] != A[i-1]):
            res.append(A[i])
            i, j = i + 1, j + 1
         elif A[i] < B[j]: i += 1
         else: j += 1
      return res

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9]
   B = [2, 4, 5, 6, 7]
   t = Solution()
   print t.intersectSortedArray(A, B)

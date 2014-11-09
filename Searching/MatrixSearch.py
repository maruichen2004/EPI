class Solution:
   # Time: O(n)
   # Space: O(1)
   def matrixSearch(self, A, k):
      i, j = 0, len(A[0]) - 1
      while i < len(A) and j >= 0:
         if A[i][j] == k: return True
         elif A[i][j] < k: i += 1
         else: j -= 1
      return False

if __name__ == "__main__":
   A = [[1, 4, 7, 10],[2, 5, 8, 11], [3, 6, 9, 12]]
   t = Solution()
   for i in range(5, 15):
      print t.matrixSearch(A, i),

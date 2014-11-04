class Solution:
   # Time: O(n^2)
   # Space: O(1)
   def rotateMatrix(self, A):
      n = len(A)
      for i in range(n):
         for j in range(n-1-i):
            A[i][j], A[n-1-j][n-1-i] = A[n-1-j][n-1-i], A[i][j]
      for i in range(n/2):
         for j in range(n):
            A[i][j], A[n-1-i][j] = A[n-1-i][j], A[i][j]

if __name__ == "__main__":
   A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   t = Solution()
   t.rotateMatrix(A)
   print A

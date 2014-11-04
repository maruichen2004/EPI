class Solution:
   # Time: O(mn)
   # Space: O(1)
   def printSpiralMatrix(self, A):
      res = []
      top, bottom, left, right = 0, len(A) - 1, 0, len(A[0]) - 1
      while top <= bottom and left <= right:
         for i in range(left, right + 1):
            res.append(A[top][i])
         for i in range(top + 1, bottom):
            res.append(A[i][right])
         for i in reversed(range(left, right + 1)):
            if top < bottom: res.append(A[bottom][i])
         for i in reversed(range(top + 1, bottom)):
            if left < right: res.append(A[i][left])
         top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
      return res

   def generateSpiralMatrix(self, n):
      num = 1
      res = [[0 for i in range(n)] for j in range(n)]
      top, bottom, left, right = 0, n - 1, 0, n - 1
      while top <= bottom and left <= right:
         for i in range(left, right + 1):
            res[top][i] = num
            num += 1
         for i in range(top + 1, bottom):
            res[i][right] = num
            num += 1
         for i in reversed(range(left, right + 1)):
            if top < bottom:
               res[bottom][i] = num
               num += 1
         for i in reversed(range(top + 1, bottom)):
            res[i][left] = num
            num += 1
         top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
      return res

if __name__ == "__main__":
   A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
   t = Solution()
   print t.printSpiralMatrix(A)
   n = 3
   print t.generateSpiralMatrix(n)

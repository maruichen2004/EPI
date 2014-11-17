class Solution:
   # Time: O(n + m)
   # Space: O(1)
   def mergeTwoSortedArray(self, A, m, B, n):
      i, j = m - 1, n - 1
      while i >= 0 and j >= 0:
         if A[i] > B[j]:
            A[i+j+1] = A[i]
            i -= 1
         else:
            A[i+j+1] = B[j]
            j -= 1
      while j >= 0:
         A[j] = B[j]
         j -= 1
      return A

if __name__ == "__main__":
   A = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]
   B = [2, 4, 6, 8, 10]
   m, n = 5, 5
   t = Solution()
   print t.mergeTwoSortedArray(A, m, B, n)
